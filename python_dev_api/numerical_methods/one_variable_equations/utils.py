from sympy import sympify, symbols
import numpy as np


def error_absoluto(x0, x1):
    return abs(x1-x0)


def error_relativo(x0, x1):
    return abs((x1-x0)/x1)


def call_eval_f(parameters):
    f = parameters["funcion"]
    x = parameters["x"]

    response = dict()
    response["y"] = eval_f(f, x)

    return response


def plot_f(parameters):
    f = parameters["funcion"]
    xa = parameters["xa"]
    xb = parameters["xb"]
    delta = parameters["delta"]

    xa = eval(xa)
    xb = eval(xb)
    delta = eval(delta)

    response = dict()
    response["data"] = []

    for xi in np.arange(xa, xb, delta):
        response["data"].append({"x": str(xi), "y": str(eval_f(f, xi))})

    return response


def eval_f(f, x0):
    f = sympify_expr(f)
    x = symbols("x")

    return str(f.evalf(subs={x: x0}))


def sympify_expr(f):
    if "e" in f:
        f = f.replace("e", "E")
    # if "sen" in f:
    #     f = f.replace("sen", "sin")

    return sympify(f)
