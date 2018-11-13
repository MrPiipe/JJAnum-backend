from sympy import symbols
from .one_variable_equations_parent import sympify_expr
from ..numerical_method import NumericalMethod
from .one_variable_equations_parent import absolute_error, relative_error


class FixedPoint(NumericalMethod):
    def evaluate(self, parameters):

        x = symbols("x")
        response = self.init_response()

        g = str(parameters["fx"])
        xa = float(parameters["x0"])
        n_iter = int(parameters["nIters"])
        tol = eval(parameters["tol"])
        error_type = eval(parameters["error_type"])

        calculate_error = relative_error if error_type == 2 else absolute_error

        g = sympify_expr(g)
        response["input_function"] = str(g)

        contador = 0
        error = tol + 1

        while error > tol and contador < n_iter:
            err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""

            iteracion = [contador, str(xa), err_fm]
            response["iterations"].append(iteracion)

            xn = g.evalf(subs={x: xa})

            error = calculate_error(xn, xa)

            xa = xn
            contador = contador + 1

        iteracion = [contador, str(xa), str(error)]
        response["iterations"].append(iteracion)

        if error < tol:
            response["aproximation"].append(str(xn))
        else:
            response["error"] = "The method failed after {} iterations"\
                .format(n_iter)

        return response

    def init_response(self):
        response = dict()
        response["iterations"] = []
        response["aproximation"] = []
        response["error"] = ""

        return response
