import numpy as np

from ..numerical_method import NumericalMethod
from .equation_systems_parent import exchange_cols, exchange_rows, exchange_marks, concatenate
from .equation_systems_parent import is_not_invertible, regressive_sustitution, process_params


class GaussEliminationTotalPivot(NumericalMethod):
    def evaluate(self, parameters):
        A = parameters["A"]
        b = parameters["b"]

        A, b = process_params(A, b)
        response = self.init_response()

        if is_not_invertible(A):
            response["error"] = "The matrix can not be inverted"
            return response

        augmented, marcas = elimination(A, b)

        A = np.delete(augmented.copy(), len(augmented), 1)
        b = augmented[:, len(augmented)]

        x = regressive_sustitution(A, b)
        x = organice_marks(x,  marcas)

        response["augmented"] = np.round(augmented, 4).tolist()
        response["x"] = np.round(x, 4).tolist()

        return response

    def init_response(self):
        response = dict()

        return response


def elimination(A, b):
    augmented = concatenate(A, b)

    n = len(augmented)
    marcas = np.arange(1, n+1)

    for k in range(0, n-1):
        augmented, marcas = total_pivot(augmented, marcas, n, k)
        for i in range(k+1, n):
            mult = augmented[i, k]/augmented[k, k]
            for j in range(k, n+1):
                augmented[i, j] = augmented[i, j] - mult * augmented[k, j]

    return augmented, marcas


def total_pivot(augmented, marcas, n, k):
    mayor = 0
    fila_mayor = k
    col_mayor = k
    for r in range(k, n):
        for s in range(k, n):
            if abs(augmented[r, s]) > mayor:
                mayor = abs(augmented[r, s])
                fila_mayor = r
                col_mayor = s
    if mayor == 0:
        raise Exception("The system has no unique solution")
    else:
        if fila_mayor != k:
            augmented = exchange_rows(augmented, fila_mayor, k)
        if col_mayor != k:
            augmented = exchange_cols(augmented, col_mayor, k)
            marcas = exchange_marks(marcas, col_mayor, k)
        return augmented, marcas


def organice_marks(x, marcas):
    x_sorted = np.zeros(len(marcas))

    for i in range(len(marcas)):
        pos = marcas[i] - 1
        x_sorted[pos] = x[int(i)]
    return x_sorted
