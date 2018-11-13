from sympy import symbols
from .one_variable_equations_parent import sympify_expr

from ..numerical_method import NumericalMethod


class IncrementalSearch(NumericalMethod):

    def evaluate(self, parameters):
        found = False
        response = self.init_response()
        x = symbols("x")

        f = str(parameters["fx"])
        x0 = float(parameters["x0"])
        delta = float(parameters["delta"])
        n_iter = int(parameters["nIters"])

        f = sympify_expr(f)
        response["input_function"] = str(f)
        fx0 = f.evalf(subs={x: x0})

        if fx0 == 0:
            response["roots"].append(x0)

        x1 = x0 + delta
        contador = 0
        fx1 = f.evalf(subs={x: x1})

        while contador < n_iter:
            iteracion = [contador, str(x0), str(fx0)]
            response["iterations"].append(iteracion)

            if fx1 == 0:
                response["roots"].append(x1)
                found = True

            elif fx0 * fx1 < 0:
                response["intervals"].append([x0, x1])
                found = True

            x0 = x1
            fx0 = fx1
            x1 = x0 + delta
            fx1 = f.evalf(subs={x: x1})
            contador = contador + 1

        if not found:
            response["error"] = "The method failed after {} iterations".format(n_iter)

        return response

    def init_response(self):
        response = dict()
        response["roots"] = []
        response["intervals"] = []
        response["iterations"] = []
        response["error"] = ""

        return response
