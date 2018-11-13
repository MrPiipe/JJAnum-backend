import numpy as np
from sympy import sympify

from ..numerical_method import NumericalMethod
from .interpolation_parent import process_params, evaluate_splines


class CuadraticSpline(NumericalMethod):
    def evaluate(self, parameters):
        X = parameters["X"]
        Y = parameters["Y"]
        x_eval = eval(parameters["eval"])

        puntos = process_params(X, Y)

        n = len(puntos) - 1
        puntos = np.array(puntos)
        matrix = np.zeros((n*3, n*3))
        independent_vector = np.zeros(n*3)

        j = 0
        k = 0
        for i in range(0, n*2, 2):
            matrix[i, j+0] = puntos[k, 0] ** 2
            matrix[i, j+1] = puntos[k, 0]
            matrix[i, j+2] = 1

            matrix[i+1, j+0] = puntos[k+1, 0] ** 2
            matrix[i+1, j+1] = puntos[k+1, 0]
            matrix[i+1, j+2] = 1

            j += 3
            k += 1

        j = 1
        k = 0
        for i in range(n*2, n*3-1):
            matrix[i][k + 0] = 2 * puntos[j, 0]
            matrix[i][k + 1] = 1

            matrix[i][k + 2+1] = - 2 * puntos[j, 0]
            matrix[i][k + 3+1] = - 1
            j += 1
            k += 3

        matrix[n*3-1, 0] = 1

        independent_vector[0] = puntos[0, 1]
        j = 1
        for i in range(1, n):
            independent_vector[j] = puntos[i, 1]
            independent_vector[j+1] = puntos[i, 1]
            j += 2
        independent_vector[n*2-1] = puntos[n, 1]

        print(matrix)
        print(independent_vector)

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

        for i in range(0, n*3, 3):
            funcion = "{a}*x**2 + {b}*x + {c}".format(
                a=coeficientes[i],
                b=coeficientes[i+1],
                c=coeficientes[i+2],
            )

            funcion = str(sympify(funcion).expand())
            funcion_partes.append([funcion, "{x0} <= x <= {x1}".format(
                x0=puntos[i//3, 0],
                x1=puntos[i//3+1, 0]
            )])

        return funcion_partes
