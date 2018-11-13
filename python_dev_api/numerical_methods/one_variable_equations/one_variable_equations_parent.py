from sympy import sympify, symbols
import numpy as np


def absolute_error(x0, x1):
    return abs(x1-x0)


def relative_error(x0, x1):
    return abs((x1-x0)/x1)


def call_eval_function(parameters):
    f = parameters["inputFunction"]
    x = parameters["x"]

    response = dict()
    response["y"] = eval_function(f, x)

    return response


def plot_function(parameters):
    f = parameters["inputFunction"]
    xa = parameters["xa"]
    xb = parameters["xb"]
    delta = parameters["delta"]

    xa = eval(xa)
    xb = eval(xb)
    delta = eval(delta)

    response = dict()
    response["data"] = []

    for xi in np.arange(xa, xb, delta):
        response["data"].append({"x": str(xi), "y": str(eval_function(f, xi))})

    return response


def eval_function(f, x0):
    f = sympify_expr(f)
    x = symbols("x")

    return str(f.evalf(subs={x: x0}))


def sympify_expr(f):
    # if "e" in f:
    #     f = f.replace("e", "E")

    return sympify(f)
