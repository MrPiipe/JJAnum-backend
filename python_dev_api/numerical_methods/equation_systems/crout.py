import numpy as np

from ..numerical_method import NumericalMethod
from .equation_systems_parent import progressive_sustitution, regressive_sustitution, process_params, is_not_invertible


class Crout(NumericalMethod):
    def evaluate(self, parameters):
        A = parameters["A"]
        b = parameters["b"]

        A, b = process_params(A, b)

        response = self.init_response()

        if is_not_invertible(A):
            response["error"] = "The matrix can not be inverted"
            return response

        n = len(A)
        L = np.identity(n)
        U = np.identity(n)

        for k in range(n):
            suma1 = 0

            for p in range(k):
                suma1 = suma1 + L[k, p]*U[p, k]
            L[k, k] = A[k, k]-suma1

            for i in range(k+1, n):
                suma2 = 0
                for p in range(0, k):
                    suma2 = suma2 + L[i, p]*U[p, k]
                L[i, k] = (A[i, k]-suma2)/U[k, k]
            for j in range(k+1, n):
                suma3 = 0
                for p in range(0, k):
                    suma3 = suma3 + L[k, p] * U[p, j]
                U[k, j] = (A[k, j]-suma3)/L[k, k]

        z = progressive_sustitution(L, b)
        x = regressive_sustitution(U, z)

        response["L"] = np.round(L, 4).tolist()
        response["U"] = np.round(U, 4).tolist()
        response["z"] = np.round(z, 4).tolist()
        response["x"] = np.round(x, 4).tolist()

        return response

    def init_response(self):
        response = dict()

        return response
