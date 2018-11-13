from sympy import symbols
from .one_variable_equations_parent import sympify_expr
from ..numerical_method import NumericalMethod
from .one_variable_equations_parent import absolute_error, relative_error


class Newton(NumericalMethod):
    def evaluate(self, params):
        tol = eval(params["tol"])
        xa = eval(params["x0"])
        n_iter = eval(params["nIters"])
        f = params["fx"]
        f_prima = params["dfx"]
        error_type = eval(params["error_type"])

        calculate_error = relative_error if error_type == 2 else absolute_error

        response = self.init_response()
        contador = 0
        error = tol + 1

        f = sympify_expr(f)
        f_prima = sympify_expr(f_prima)
        x = symbols("x")

        response["input_function"] = str(f)
        response["der_in"] = str(f_prima)

        fx = f.evalf(subs={x: xa})
        dfx = f_prima.evalf(subs={x: xa})

        while error > tol and fx != 0 and dfx != 0 and contador < n_iter:
            err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""
            fx_fm = "{fx:.2e}".format(fx=fx)

            iteracion = [contador, str(xa), fx_fm, err_fm]
            response["iterations"].append(iteracion)

            xn = xa - fx/dfx
            fx = f.evalf(subs={x: xn})
            dfx = f_prima.evalf(subs={x: xn})

            error = calculate_error(xn, xa)
            xa = xn
            contador = contador + 1

        fx_fm = "{fx:.2e}".format(fx=fx)
        err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""
        iteracion = [contador, str(xa), fx_fm, err_fm]
        response["iterations"].append(iteracion)

        if fx == 0:
            # response["root"] = str(xa)
            response["aproximation"] = str(xn)
        elif error < tol:
            response["aproximation"] = str(xn)
        elif dfx == 0:
            response["error"] = "{} is a possible multiple root".format(xn)
        else:
            response["error"] = "The method failed after {} iterations"\
                .format(n_iter)

        return response

    def init_response(self):
        response = dict()
        response["iterations"] = []
        response["error"] = ""

        return response
