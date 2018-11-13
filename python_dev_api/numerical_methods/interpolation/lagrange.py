import numpy as np
from sympy import sympify, simplify

from ..numerical_method import NumericalMethod
from ..one_variable_equations import one_variable_equations_parent


class Lagrange(NumericalMethod):
    def evaluate(self, parameters):
        x = parameters["X"]
        y = parameters["Y"]
        x_eval = parameters["eval"]

        x = self.process_params(x)
        y = self.process_params(y)

        respuesta = ""
        n = len(x)
        res = ["" for x in range(n)]
        numerador = ""
        denominador = ""
        polinomio = ""

        for i in range(0, n):
            numerador = ""
            denominador = ""
            for j in range(0, n):
                if j is not i:
                    numerador += "(x" + "-" + str(x[j]) + ")*"
                    denominador += ("("+str(x[i]) + "-" + str(x[j]) + ")*")
            numerador = numerador[:-1]
            denominador = denominador[:-1]
            aux = str(y[i]) + "*(" + numerador + ")/(" + denominador + ")"
            res[i] = aux

        for i in res:
            polinomio += "(" + i + ")" + "+"
        polinomio = polinomio[:-1]

        polinomio = sympify(polinomio)
        polinomio = simplify(polinomio)
        polinomio = str(polinomio)
        respuesta = "p(x) = " + polinomio

        y_eval = one_variable_equations_parent.eval_function(polinomio, x_eval)
        y_eval = round(eval(y_eval), 2)

        return {"resultingFunction": respuesta, "y_eval": y_eval}

    def process_params(self, array):
        n = len(array)
        new_vector = np.zeros(n)

        for i in range(n):
            new_vector[i] = array[str(i)]

        return new_vector
