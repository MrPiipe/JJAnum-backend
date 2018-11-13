import numpy as np

from ..numerical_method import NumericalMethod
from .equation_systems_parent import concatenate, exchange_rows, regressive_sustitution, is_not_invertible, process_params


class GaussEliminationPartialPivot(NumericalMethod):
    def evaluate(self, parameters):
        A = parameters["A"]
        b = parameters["b"]

        A, b = process_params(A, b)

        response = self.init_response()

        if is_not_invertible(A):
            response["error"] = "The matrix can not be inverted"
            return response

        augmented = elimination(A, b)

        A = np.delete(augmented.copy(), len(augmented), 1)
        b = augmented[:, len(augmented)]
        x = regressive_sustitution(A, b)

        response["augmented"] = np.round(augmented, 4).tolist()
        response["x"] = np.round(x, 4).tolist()

        return response

    def init_response(self):
        response = dict()

        return response


def partial_pivot(augmented, n, k):
    mayor = abs(augmented[k, k])
    fila_mayor = k
    for s in range(k+1, n):
        if abs(augmented[s, k]) > mayor:
            mayor = abs(augmented[s, k])
            fila_mayor = s
    if mayor == 0:
        raise Exception("The system has no solution")
    else:
        if fila_mayor != k:
            augmented = exchange_rows(augmented, fila_mayor, k)
        return augmented


def elimination(A, b):
    augmented = concatenate(A, b)

    n = len(augmented)

    for k in range(0, n-1):
        augmented = partial_pivot(augmented, n, k)
        for i in range(k+1, n):
            mult = augmented[i, k]/augmented[k, k]
            for j in range(k, n+1):
                augmented[i, j] = augmented[i, j] - mult * augmented[k, j]

    return augmented
