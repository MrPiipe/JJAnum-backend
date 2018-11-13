import numpy as np

from ..numerical_method import NumericalMethod
from .equation_systems_parent import regressive_sustitution, progressive_sustitution, exchange_rows
from .equation_systems_parent import is_not_invertible, process_params


class GaussFactorizationPivot(NumericalMethod):
    def evaluate(self, parameters):
        A = parameters["A"]
        b = parameters["b"]

        A, b = process_params(A, b)
        response = self.init_response()

        if is_not_invertible(A):
            response["error"] = "The matrix can not be inverted"
            return response

        U, L, P = factorization(A)
        Bn = np.matmul(P, b.T)

        z = progressive_sustitution(L, Bn.T)
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


def factorization(A):
    n = len(A)
    P = np.identity(n)
    L = np.zeros((n, n))

    for k in range(0, n):
        A, P, L = pivot(A, P, L, k)
        for i in range(k+1, n):
            mult = A[i, k]/A[k, k]
            if i > k:
                L[i][k] = mult
            for j in range(k, n):
                A[i, j] = A[i, j] - mult * A[k, j]

    for i in range(n):
        L[i, i] = 1

    return A, L, P


def pivot(A, P, L, k):
    n = len(A)
    mayor = abs(A[k, k])
    fila_mayor = k

    for s in range(k+1, n):
        if abs(A[s, k]) > mayor:
            mayor = abs(A[s, k])
            fila_mayor = s
    if mayor == 0:
        raise Exception("The system has no solution")
    else:
        if fila_mayor != k:
            A = exchange_rows(A, fila_mayor, k)
            P = exchange_rows(P, fila_mayor, k)
            L = exchange_rows(L, fila_mayor, k)
        return A, P, L
