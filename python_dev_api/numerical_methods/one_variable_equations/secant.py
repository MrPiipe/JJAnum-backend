from sympy import symbols
from .one_variable_equations_parent import sympify_expr
from ..numerical_method import NumericalMethod
from .one_variable_equations_parent import absolute_error, relative_error


class Secant(NumericalMethod):
    def evaluate(self, params):
        tol = eval(params["tol"])
        n_iter = eval(params["nIters"])
        x0 = eval(params["x0"])
        x1 = eval(params["x1"])
        f = params["fx"]
        error_type = eval(params["error_type"])

        calculate_error = relative_error if error_type == 2 else absolute_error

        response = self.init_response()
        contador = 0
        error = tol + 1

        x = symbols("x")
        f = sympify_expr(f)

        response["input_function"] = str(f)

        fx0 = f.evalf(subs={x: x0})
        if fx0 == 0:
            response["root"] = str(x0)
            return response

        fx1 = f.evalf(subs={x: x1})
        den = fx1 - fx0

        while error > tol and fx1 != 0 and den != 0 and contador < n_iter:
            err_fm = "{e:.2e}".format(
                e=error) if contador != 0 and contador != 1 else ""
            fx0_fm = "{fx0:.2e}".format(fx0=fx0)
            iteracion = [contador, str(x0), fx0_fm, err_fm]

            response["iterations"].append(iteracion)

            x2 = x1 - fx1 * (x1 - x0)/den

            error = calculate_error(x2, x1)
            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = f.evalf(subs={x: x1})
            den = fx1 - fx0
            contador = contador+1

        iteracion = [contador, str(x0), str(fx0), str(error)]
        response["iterations"].append(iteracion)

        if fx1 == 0:
            response["aproximation"] = str(x1)
        elif error < tol:
            response["aproximation"] = str(x1)
        elif den == 0:
            response["error"] = "Possible multiple root"
        else:
            response["error"] = "The method failed after {} iterations".format(n_iter)

        return response

    def init_response(self):
        response = dict()
        response["iterations"] = []
        response["error"] = ""

        return response
