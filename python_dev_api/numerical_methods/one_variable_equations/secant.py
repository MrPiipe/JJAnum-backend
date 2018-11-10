from sympy import symbols
from .utils import sympify_expr
from ..numerical_method import NumericalMethod
from .utils import error_absoluto, error_relativo


class Secant(NumericalMethod):
    def calculate(self, params):
        tol = eval(params["tol"])
        n_iter = eval(params["nIters"])
        x0 = eval(params["x0"])
        x1 = eval(params["x1"])
        f = params["fx"]
        tipo_error = eval(params["tipo_error"])

        calcular_error = error_relativo if tipo_error == 2 else error_absoluto

        response = self.init_response()
        contador = 0
        error = tol + 1

        x = symbols("x")
        f = sympify_expr(f)

        response["funcion_in"] = str(f)

        fx0 = f.evalf(subs={x: x0})
        if fx0 == 0:
            response["raiz"] = str(x0)
            return response

        fx1 = f.evalf(subs={x: x1})
        den = fx1 - fx0

        while error > tol and fx1 != 0 and den != 0 and contador < n_iter:
            err_fm = "{e:.2e}".format(
                e=error) if contador != 0 and contador != 1 else ""
            fx0_fm = "{fx0:.2e}".format(fx0=fx0)
            iteracion = [contador, str(x0), fx0_fm, err_fm]

            response["iteraciones"].append(iteracion)

            x2 = x1 - fx1 * (x1 - x0)/den

            error = calcular_error(x2, x1)
            # error = abs(x2-x1)
            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = f.evalf(subs={x: x1})
            den = fx1 - fx0
            contador = contador+1

        iteracion = [contador, str(x0), str(fx0), str(error)]
        response["iteraciones"].append(iteracion)

        if fx1 == 0:
            # response["raiz"] = str(x1)
            response["aproximacion"] = str(x1)
        elif error < tol:
            response["aproximacion"] = str(x1)
        elif den == 0:
            response["error"] = "Posible raiz multiple"
        else:
            response["error"] = "fracasó en {} iteraciones".format(n_iter)

        return response

    def get_description(self):
        return "Halla la raíz de una función por medio del método de \
        la secante", "Se necesita tol, n_iter, x0, x1, funcion"

    def init_response(self):
        response = dict()
        response["iteraciones"] = []
        response["error"] = ""

        return response
