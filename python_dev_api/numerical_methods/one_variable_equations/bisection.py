from .one_variable_equations_parent import sympify_expr
from .one_variable_equations_parent import absolute_error, relative_error
from sympy import symbols

from ..numerical_method import NumericalMethod


class Bisection(NumericalMethod):

    def evaluate(self, parameters):
        response = self.init_response()
        x = symbols("x")

        f = str(parameters["fx"])
        xa = float(parameters["xa"])
        xb = float(parameters["xb"])
        n_iter = int(parameters["nIters"])
        tol = eval(parameters["tole"])
        error_type = eval(parameters["error_type"])

        calculate_error = relative_error if error_type == 2 else absolute_error

        f = sympify_expr(f)
        response["input_function"] = str(f)

        fxa = f.evalf(subs={x: xa})
        fxb = f.evalf(subs={x: xb})

        if abs(fxa) == 0:
            response["roots"].append(xa)

        if abs(fxb) == 0:
            response["roots"].append(xb)

        if fxa * fxb > 0:
            response["error"] = "Inadequate Interval"
            return response

        xm = (xb+xa)/2
        fxm = f.evalf(subs={x: xm})
        contador = 0
        error = tol + 1

        while error > tol and fxm != 0 and contador < n_iter:
            err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""
            fxm_fm = "{fxm:.2e}".format(fxm=fxm)

            iteracion = [contador, str(xa), str(xb), str(xm), fxm_fm, err_fm]

            response["iterations"].append(iteracion)

            if fxa * fxm < 0:
                xb = xm
                fxb = fxm
            elif fxm * fxb < 0:
                xa = xm
                fxa = fxm
            else:
                response["error"] = "Something went wrong"

            x_ant = xm
            xm = (xa+xb)/2
            fxm = f.evalf(subs={x: xm})
            error = calculate_error(xm, x_ant)
            contador = contador + 1

        err_fm = "{e:.2e}".format(e=error) if contador != 0 else ""
        fxm_fm = "{fxm:.2e}".format(fxm=fxm)
        iteracion = [contador, str(xa), str(xb), str(xm), fxm_fm, err_fm]
        response["iterations"].append(iteracion)

        if fxm == 0:
            response["aproximations"].append(str(xm))

        elif error < tol:
            response["aproximations"].append(str(xm))

        else:
            response["error"] = "The method failed after {} \
                iterations".format(n_iter)

        return response

    def init_response(self):
        response = dict()
        response["roots"] = []
        response["iterations"] = []
        response["aproximations"] = []
        response["error"] = ""

        return response
