from sympy import symbols
from .one_variable_equations_parent import sympify_expr
from ..numerical_method import NumericalMethod
from .one_variable_equations_parent import absolute_error, relative_error


class MultipleRoots(NumericalMethod):

    def evaluate(self, params):
        tol = eval(params["tol"])
        xa = eval(params["x0"])
        n_iter = eval(params["nIters"])
        f = params["fx"]
        f_prima = params["dfx"]
        f_dos_prima = params["d2fx"]
        error_type = eval(params["error_type"])

        calculate_error = relative_error if error_type == 2 else absolute_error

        response = self.init_response()
        contador = 0
        error = tol + 1

        x = symbols("x")
        f = sympify_expr(f)
        f_prima = sympify_expr(f_prima)
        f_dos_prima = sympify_expr(f_dos_prima)

        response["input_function"] = str(f)
        response["prime_f"] = str(f_prima)
        response["double_prime_f"] = str(f_dos_prima)

        fx = f.evalf(subs={x: xa})
        dfx = f_prima.evalf(subs={x: xa})
        d2fx = f_dos_prima.evalf(subs={x: xa})
        denominador = (dfx**2)-(fx*d2fx)

        while ((error > tol) and (fx != 0) and (denominador != 0) and
               (contador < n_iter)):

            err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""
            fx_fm = "{fx:.2e}".format(fx=fx)

            iteracion = [contador, str(xa), fx_fm, err_fm]

            response["iterations"].append(iteracion)

            xn = xa - (fx*dfx)/denominador

            fx = f.evalf(subs={x: xn})
            dfx = f_prima.evalf(subs={x: xn})
            d2fx = f_dos_prima.evalf(subs={x: xn})
            denominador = (dfx**2)-(fx*d2fx)

            error = calculate_error(xn, xa)
            xa = xn
            contador = contador + 1

        fx_fm = "{fx:.2e}".format(fx=fx)
        err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""
        iteracion = [contador, str(xa), fx_fm, err_fm]
        response["iterations"].append(iteracion)

        if fx == 0:
            response["aproximation"] = str(xn)

        elif error < tol:
            response["aproximation"] = str(xn)
        elif denominador == 0:
            response["error"] = "Denominator is 0"

        else:
            response["error"] = "The method failed after {} iterations"\
                .format(n_iter)

        return response

    def init_response(self):
        response = dict()
        response["iterations"] = []
        response["error"] = ""

        return response
