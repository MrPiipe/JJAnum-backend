from sympy import symbols
from .utils import sympify_expr

from ..numeric_method import NumericMethod


class IncrementalSearch(NumericMethod):

    def calculate(self, parameters):
        # Se crean las variables
        found = False
        response = self.init_response()
        x = symbols("x")

        # Extracción de los parametros
        f = str(parameters["fx"])
        x0 = float(parameters["x0"])
        delta = float(parameters["delta"])
        n_iter = int(parameters["nIters"])

        # Transformar f a sympy
        f = sympify_expr(f)
        response["funcion_in"] = str(f)
        fx0 = f.evalf(subs={x: x0})

        if fx0 == 0:
            response["raices"].append(x0)

        x1 = x0 + delta
        contador = 0
        fx1 = f.evalf(subs={x: x1})

        while contador < n_iter:
            iteracion = [contador, str(x0), str(fx0)]
            response["iteraciones"].append(iteracion)

            if fx1 == 0:
                response["raices"].append(x1)
                found = True
                # print(x1, "es raíz")

            elif fx0 * fx1 < 0:
                response["intervalos"].append([x0, x1])
                found = True
                # print("Hay una raíz entre {} y {}".format(x0, x1))

            x0 = x1
            fx0 = fx1
            x1 = x0 + delta
            fx1 = f.evalf(subs={x: x1})
            contador = contador + 1

        if not found:
            # print("Se fracasó en {} intentos".format(n_iter))
            response["error"] = "Se fracasó en {} intentos".format(n_iter)

        return response

    def get_description(self):
        return "Este método se encarga de encontrar un intervalos con raíces",
        "se necesita funcion, x0, delta y n_iter"

    def init_response(self):
        response = dict()
        response["raices"] = []
        response["intervalos"] = []
        response["iteraciones"] = []
        response["error"] = ""

        return response
