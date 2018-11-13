import numpy as np
from ..numerical_method import NumericalMethod
from .interpolation_parent import process_params
from ..one_variable_equations import one_variable_equations_parent


class Vandermonde(NumericalMethod):
    def evaluate(self, parameters):
        X = parameters["X"]
        Y = parameters["Y"]
        x_eval = parameters["eval"]

        puntos = process_params(X, Y)

        n = len(puntos)
        matriz_vandermonde = []

        for i in range(n):
            x = puntos[i][0]
            fila = self.generate_equation(x, n)
            matriz_vandermonde.append(fila)

        matriz_vandermonde = np.array(matriz_vandermonde)
        b = puntos[:, 1].copy()

        vector_a = np.linalg.solve(matriz_vandermonde, b)
        funcion = self.generate_function(np.round(vector_a, 4))
        y_eval = one_variable_equations_parent.eval_function(funcion[7:], x_eval)

        return {
            "resultingFunction": funcion,
            "matrix": np.round(matriz_vandermonde, 4).tolist(),
            "y_eval": round(eval(y_eval), 2)
            }

    def generate_function(self, coeficientes):
        n = len(coeficientes)
        funcion = "p(x) = "
        for i in range(n-1):
            if coeficientes[i] == 0.0:
                continue
            funcion = funcion + str(coeficientes[i]) + "*x^" + str(n-i-1) + " + "

        funcion = funcion + str(coeficientes[n-1])
        return funcion

    def generate_equation(self, x, n):
        coeficientes = []
        for i in range(n-1, -1, -1):
            coeficientes.append(x**i)

        return np.array(coeficientes)
