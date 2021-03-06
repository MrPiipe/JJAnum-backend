import numpy as np

from ..numerical_method import NumericalMethod
from .equation_systems_parent import progressive_sustitution, regressive_sustitution, is_not_invertible, process_params


class Doolittle(NumericalMethod):
    def evaluate(self, parameters):
        A = parameters["A"]
        b = parameters["b"]

        matrix, b = process_params(A, b)
        response = self.init_response()

        if is_not_invertible(matrix):
            response["error"] = "The matrix can not be inverted"
            return response

        n = len(matrix)
        L = np.identity(n)
        U = np.identity(n)

        for k in range(n):
            suma1 = 0

            for p in range(k):
                suma1 = suma1 + L[k, p]*U[p, k]
            U[k, k] = matrix[k, k]-suma1

            for i in range(k+1, n):
                suma2 = 0
                for p in range(0, k):
                    suma2 = suma2 + L[i, p]*U[p, k]
                L[i, k] = (matrix[i, k]-suma2)/U[k, k]
            for j in range(k+1, n):
                suma3 = 0
                for p in range(k):
                    suma3 = suma3 + L[k, p] * U[p, j]
                U[k, j] = (matrix[k, j]-suma3)/L[k, k]

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
