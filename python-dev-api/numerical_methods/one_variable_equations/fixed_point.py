from sympy import symbols
from .utils import sympify_expr
from ..numeric_method import NumericMethod
from .utils import error_absoluto, error_relativo


class FixedPoint(NumericMethod):
    def calculate(self, parameters):

        x = symbols("x")
        response = self.init_response()

        # Extracción de los parametros
        g = str(parameters["fx"])
        xa = float(parameters["x0"])
        n_iter = int(parameters["nIters"])
        tol = eval(parameters["tol"])
        tipo_error = eval(parameters["tipo_error"])

        calcular_error = error_relativo if tipo_error == 2 else error_absoluto

        # Transformar g a sympy
        g = sympify_expr(g)
        response["funcion_in"] = str(g)

        contador = 0
        error = tol + 1

        while error > tol and contador < n_iter:
            err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""

            iteracion = [contador, str(xa), err_fm]
            response["iteraciones"].append(iteracion)

            xn = g.evalf(subs={x: xa})

            error = calcular_error(xn, xa)

            xa = xn
            contador = contador + 1

        iteracion = [contador, str(xa), str(error)]
        response["iteraciones"].append(iteracion)

        if error < tol:
            response["aproximado"].append(str(xn))
        else:
            response["error"] = "El método fracasó en {} iteraciones"\
                .format(n_iter)

        return response

    def get_description(self):
        return "Este metodo encuentra el punto fijo de una función x = g(x)",
        "Se necesita funcion, xa, n_iter, y tol"

    def init_response(self):
        response = dict()
        response["iteraciones"] = []
        response["aproximado"] = []
        response["error"] = ""

        return response
