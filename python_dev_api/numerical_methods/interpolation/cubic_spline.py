import numpy as np
from sympy import sympify

from ..numerical_method import NumericalMethod
from .interpolation_parent import process_params, evaluate_splines


class CubicSpline(NumericalMethod):
    def evaluate(self, parameters):
        X = parameters["X"]
        Y = parameters["Y"]
        x_eval = eval(parameters["eval"])

        puntos = process_params(X, Y)

        n = len(puntos) - 1
        puntos = np.array(puntos)
        matrix = np.zeros((n*4, n*4))
        independent_vector = np.zeros(n*4)

        j = 0
        k = 0
        for i in range(0, n*2-1, 2):
            matrix[i, j+0] = puntos[k, 0] ** 3
            matrix[i, j+1] = puntos[k, 0] ** 2
            matrix[i, j+2] = puntos[k, 0]
            matrix[i, j+3] = 1

            matrix[i+1, j+0] = puntos[k+1, 0] ** 3
            matrix[i+1, j+1] = puntos[k+1, 0] ** 2
            matrix[i+1, j+2] = puntos[k+1, 0]
            matrix[i+1, j+3] = 1

            j += 4
            k += 1

        j = 1
        k = 0
        for i in range(n*2, n*3-1):
            matrix[i][k + 0] = 3 * puntos[j, 0]**2
            matrix[i][k + 1] = 2 * puntos[j, 0]
            matrix[i][k + 2] = 1

            matrix[i][k + 3+1] = - 3 * puntos[j, 0]**2
            matrix[i][k + 4+1] = - 2 * puntos[j, 0]
            matrix[i][k + 5+1] = - 1
            j += 1
            k += 4

        j = 1
        k = 0
        for i in range(n*3-1, n*4-2):
            matrix[i][k + 0] = 6 * puntos[j, 0]
            matrix[i][k + 1] = 2

            matrix[i][k + 3+1] = - 6 * puntos[j, 0]
            matrix[i][k + 4+1] = - 2
            j += 1
            k += 4

        matrix[n*4-2, 0] = 6 * puntos[0, 0]
        matrix[n*4-2, 1] = 2

        matrix[n*4-1, n*4-4] = 6 * puntos[n, 0]
        matrix[n*4-1, n*4-3] = 2

        independent_vector[0] = puntos[0, 1]
        j = 1
        for i in range(1, n):
            independent_vector[j] = puntos[i, 1]
            independent_vector[j+1] = puntos[i, 1]
            j += 2
        independent_vector[n*2-1] = puntos[n, 1]

        sol = np.linalg.solve(matrix, independent_vector)
        funcion = self.generate_equation(sol, puntos)

        try:
            y_eval = evaluate_splines(funcion, puntos, x_eval)
        except Exception as e:
            return {"resultingFunction": funcion, "error": str(e)}

        return {"resultingFunction": funcion, "y_eval": y_eval}

    def generate_equation(self, coeficientes, puntos):
        funcion_partes = []
        coeficientes = np.round(coeficientes, 2)
        n = len(puntos) - 1

        j = 0
        for i in range(0, n*4, 4):
            funcion = "{a}*x**3 + {b}*x**2 + {c}*x + {d}".format(
                a=coeficientes[i],
                b=coeficientes[i+1],
                c=coeficientes[i+2],
                d=coeficientes[i+3],
            )

            funcion = str(sympify(funcion).expand())
            funcion_partes.append([funcion, "{x0} <= x <= {x1}".format(
                    x0=puntos[j, 0],
                    x1=puntos[j+1, 0]
                )])

            j += 1

        return funcion_partes
