import numpy as np
from sympy import sympify


from ..numerical_method import NumericalMethod
from .interpolation_parent import process_params, evaluate_splines


class LinearSpline(NumericalMethod):
    def evaluate(self, parameters):
        X = parameters["X"]
        Y = parameters["Y"]
        x_eval = eval(parameters["eval"])

        puntos = process_params(X, Y)

        puntos = np.array(puntos)
        n = len(puntos)
        splines = []
        for i in range(n-1):
            recta = self.calculate_vector(puntos[i], puntos[i+1])
            splines.append(recta)

        funcion = []
        for i in range(n-1):
            funcion.append([splines[i], "{x0} <= x <= {x1}".format(
                x0=puntos[i][0], x1=puntos[i+1][0])])

        try:
            y_eval = evaluate_splines(funcion, puntos, x_eval)
        except Exception as e:
            return {"resultingFunction": funcion, "error": str(e)}
        return {"resultingFunction": funcion, "y_eval": y_eval}

    def calculate_vector(self, punto0, punto1):
        recta = "{fx1} + ({fx1} - {fx0})/({x1} - {x0})*(x - {x1})".format(
            fx1=punto1[1],
            fx0=punto0[1],
            x1=punto1[0],
            x0=punto0[0])

        return str(sympify(recta).expand())
