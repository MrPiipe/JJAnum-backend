from sympy import symbols
from .utils import sympify_expr
from ..numerical_method import NumericalMethod
from .utils import error_absoluto, error_relativo


class Newton(NumericalMethod):

    def calculate(self, params):
        tol = eval(params["tol"])
        xa = eval(params["x0"])
        n_iter = eval(params["nIters"])
        f = params["fx"]
        f_prima = params["dfx"]
        tipo_error = eval(params["tipo_error"])

        calcular_error = error_relativo if tipo_error == 2 else error_absoluto

        response = self.init_response()
        contador = 0
        error = tol + 1

        f = sympify_expr(f)
        f_prima = sympify_expr(f_prima)
        x = symbols("x")

        response["funcion_in"] = str(f)
        response["der_in"] = str(f_prima)

        fx = f.evalf(subs={x: xa})
        dfx = f_prima.evalf(subs={x: xa})

        while error > tol and fx != 0 and dfx != 0 and contador < n_iter:
            err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""
            fx_fm = "{fx:.2e}".format(fx=fx)

            iteracion = [contador, str(xa), fx_fm, err_fm]
            response["iteraciones"].append(iteracion)

            xn = xa - fx/dfx
            fx = f.evalf(subs={x: xn})
            dfx = f_prima.evalf(subs={x: xn})

            error = calcular_error(xn, xa)
            # error = abs((xn-xa))
            xa = xn
            contador = contador + 1

        fx_fm = "{fx:.2e}".format(fx=fx)
        err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""
        iteracion = [contador, str(xa), fx_fm, err_fm]
        response["iteraciones"].append(iteracion)

        if fx == 0:
            # response["raiz"] = str(xa)
            response["aproximado"] = str(xn)
        elif error < tol:
            response["aproximado"] = str(xn)
        elif dfx == 0:
            response["error"] = "{} es una posible raíz multiple".format(xn)
        else:
            response["error"] = "El método fracasó en {} iteraciones"\
                .format(n_iter)

        return response

    def get_description(self):
        return "Este metodo encuentra la raiz de una función a través del \
            metodo de Newton", "Se necesita tol, x0, n_iter, funcion y f_prima"

    def init_response(self):
        response = dict()
        response["iteraciones"] = []
        response["error"] = ""

        return response
