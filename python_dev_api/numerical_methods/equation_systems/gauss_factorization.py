import numpy as np

from ..numerical_method import NumericalMethod
from .equation_systems_parent import regressive_sustitution, progressive_sustitution, is_not_invertible, process_params


class GaussFactorization(NumericalMethod):
    def evaluate(self, parameters):
        A = parameters["A"]
        b = parameters["b"]

        A, b = process_params(A, b)
        response = self.init_response()

        if is_not_invertible(A):
            response["error"] = "The matrix can not be inverted"
            return response

        L, U = factorization(A, b)
        z = progressive_sustitution(L, b)
        x = regressive_sustitution(U, z)

        L = np.round(L, 2)
        U = np.round(U, 2)

        response["L"] = np.round(L, 4).tolist()
        response["U"] = np.round(U, 4).tolist()

        response["z"] = np.round(z, 4).tolist()
        response["x"] = np.round(x, 4).tolist()

        return response

    def init_response(self):
        response = dict()

        return response


def factorization(matrix, vector):
    n = len(matrix)

    L = np.identity(n)
    U = np.zeros((n, n))

    m_augm = np.concatenate((matrix, vector.T), axis=1)

    for k in range(0, n-1):
        for i in range(k+1, n):
            multiplier = m_augm[i, k]/m_augm[k, k]
            if i > k:
                L[i][k] = multiplier
            for j in range(k, n+1):
                m_augm[i, j] = m_augm[i, j] - multiplier * m_augm[k, j]

    U = m_augm.copy()
    U = np.delete(U, n, axis=1)

    return L, U
