import numpy as np
from ..numerical_method import NumericalMethod
from .interpolation_parent import process_params
from ..one_variable_equations import one_variable_equations_parent


class NewtonInterpolation(NumericalMethod):
    def evaluate(self, parameters):
        X = parameters["X"]
        Y = parameters["Y"]
        x_eval = parameters["eval"]

        puntos = process_params(X, Y)

        n = len(puntos)

        matrix = np.zeros((n, n+1))
        for i in range(n):
            matrix[i, 0] = puntos[i, 0]
            matrix[i, 1] = puntos[i, 1]

        k = 1
        for i in range(2, n+1):
            for j in range(i, n+1):
                fxk_1 = matrix[j-1-1, i-1]
                fxk = matrix[j-1, i-1]

                xk_1 = matrix[j-1, 0]
                xk = matrix[j-1-k, 0]

                matrix[j-1, i] = (fxk - fxk_1) / (xk_1 - xk)
            k += 1

        funcion = self.generate_equation(matrix, puntos)
        y_eval = one_variable_equations_parent.eval_function(funcion[7:], x_eval)
        return {"resultingFunction": funcion, "y_eval": y_eval}

    def generate_equation(self, matrix, puntos):
        funcion = "p(x) = "

        xs = []
        for i in range(len(matrix)):
            if i != 0:
                x = np.round(puntos[i-1, 0], 2)
                xs.append("*(x - {x})".format(x=x))

            const = np.round(matrix[i, i+1], 3)

            if const == 0:
                continue
            funcion += str(const) + "".join(xs) + " + "

        return funcion[:-3]
