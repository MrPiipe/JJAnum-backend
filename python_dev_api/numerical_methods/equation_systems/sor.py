import numpy as np

from ..numerical_method import NumericalMethod
from .equation_systems_parent import zeros_in_diagonal, process_params, spectral_radius


class SOR(NumericalMethod):
    def evaluate(self, parameters):
        A = parameters["A"]
        b = parameters["b"]
        x0 = parameters["x0"]
        w = parameters["w"]
        tol = parameters["tole"]
        iteraciones = parameters["niter"]

        A, b, x0 = process_params(A, b, x0)
        b = b[0]
        tol = eval(tol)
        iteraciones = int(iteraciones)
        w = float(w)

        response = self.init_response()

        if zeros_in_diagonal(A):
            response["error"] = "The matrix contains 0s in the diagonal"
            return response

        contador = 0
        dispersion = tol + 1

        T, C = self.find_T_C(A, b, w)

        if spectral_radius(T) >= 1:
            response["error"] = "The Spectral Radius of the matrix T is more than 1, we recommend you re-organize the matrix"
            return response

        while dispersion > tol and contador < iteraciones:
            x1 = np.matmul(T, x0) + C

            disp_fmt = "{e:.2e}".format(e=dispersion) if contador != 0 else ""
            iteracion = [contador, x1.tolist(), disp_fmt]
            response["iterations"].append(iteracion)

            dispersion = np.linalg.norm(x1 - x0, 2)
            x0 = x1.copy()
            contador = contador + 1

        disp_fmt = "{e:.2e}".format(e=dispersion) if contador != 0 else ""
        iteracion = [contador, x0.tolist(), disp_fmt]
        response["iterations"].append(iteracion)

        if dispersion < tol:
            response["aproximations"].append(x1.tolist())
        else:
            response["error"] = "The method failed after {} \
                iterations, the method diverges".format(iteraciones)

        return response

    def find_T_C(self, A, b, w):
        D = np.diag(np.diag(A))
        U = -1 * (np.triu(A) - D)
        L = -1 * (np.tril(A) - D)

        D_wL_inv = np.linalg.inv(D - w*L)
        T = np.matmul(D_wL_inv, (1-w)*D + w*U)
        C = np.matmul(w * D_wL_inv, b)

        return T, C

    def error(self, x):
        return np.amax(np.absolute(x))

    def init_response(self):
        response = dict()
        response["iterations"] = []
        response["aproximations"] = []

        return response
