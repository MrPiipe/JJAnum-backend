import numpy as np

from ..numerical_method import NumericalMethod
from .equation_systems_parent import process_params, zeros_in_diagonal, spectral_radius


class Seidel(NumericalMethod):
    def evaluate(self, parameters):
        A = parameters["A"]
        b = parameters["b"]
        x0 = parameters["x0"]
        tol = parameters["tole"]
        iteraciones = parameters["niter"]

        A, b, x0 = process_params(A, b, x0)
        b = b[0]
        tol = eval(tol)
        iteraciones = int(iteraciones)

        response = self.init_response()

        if zeros_in_diagonal(A):
            response["error"] = "The matrix contains 0s in the diagonal"
            return response

        contador = 0
        dispersion = tol + 1

        T, C = self.find_T_C(A, b)

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
            response["error"] = " The method failed after {} \
                iterations".format(iteraciones)

        return response

    def find_T_C(self, A, b):
        D = np.diag(np.diag(A))
        U = -1 * (np.triu(A) - D)
        L = -1 * (np.tril(A) - D)

        D_L_inv = np.linalg.inv(D-L)
        T = np.matmul(D_L_inv, U)
        C = np.matmul(D_L_inv, b)

        return T, C

    def error(self, x):
        return np.amax(np.absolute(x))

    def init_response(self):
        response = dict()
        response["iterations"] = []
        response["aproximations"] = []

        return response
