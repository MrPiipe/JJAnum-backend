from .numerical_method import NumericalMethod

from .one_variable_equations.incremental_searches import IncrementalSearch
from .one_variable_equations.bisection import Bisection
from .one_variable_equations.false_position import FalsePosition
from .one_variable_equations.newton import Newton
from .one_variable_equations.multiple_roots import MultipleRoots 
from .one_variable_equations.fixed_point import FixedPoint
from .one_variable_equations.secant import Secant

def createMethod(method):
    method = method.lower()

    if method == "incSearch":
        return IncrementalSearch()
    elif method == "bisection":
        return Bisection()
    elif method == "falsePosition":
        return FalsePosition()
    elif method == "fixedPoint":
        return FixedPoint()
    elif method == "newton":
        return Newton()
    elif method == "multipleRoots":
        return MultipleRoots()
    elif method == "secante":
        return Secant()

    # Capitulo sistemas de ecuaciones
    # elif method == "eliminacion_simple":
    #     return EliminacionSimple()
    # elif method == "eliminacion_piv_parcial":
    #     return EliminacionPivoteoParcial()
    # elif method == "eliminacion_piv_total":
    #     return EliminacionPivoteoTotal()

    # elif method == "factorizacion_simple":
    #     return FactorizacionGaussiana()
    # elif method == "factorizacion_pivoteo":
    #     return FactorizacionPivoteo()
    # elif method == "doolittle":
    #     return FactorizacionDoolittle()
    # elif method == "crout":
    #     return FactorizacionCrout()
    # elif method == "cholesky":
    #     return FactorizacionCholesky()
    # elif method == "jacobi":
    #     return Jacobi()
    # elif method == "seidel":
    #     return Seidel()
    # elif method == "sor":
    #     return SOR()

    # # Capitulo de interpolacion
    # elif method == "interpolacion_ecuaciones":
    #     return MetodoSistemaEcuaciones()
    # elif method == "newton_diferencias":
    #     return NewtonDiferenciasDivididas()
    # elif method == "lagrange":
    #     return Lagrange()
    # elif method == "spline_lineal":
    #     return SplinesLineales()
    # elif method == "spline_cuadratico":
    #     return SplinesCuadraticos()
    # elif method == "spline_cubico":
    #     return SplinesCubicos()
    else:
        return NumericalMethod()
