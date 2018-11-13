from .numerical_method import NumericalMethod

from .one_variable_equations.incremental_searches import IncrementalSearch
from .one_variable_equations.bisection import Bisection
from .one_variable_equations.false_position import FalsePosition
from .one_variable_equations.newton import Newton
from .one_variable_equations.multiple_roots import MultipleRoots 
from .one_variable_equations.fixed_point import FixedPoint
from .one_variable_equations.secant import Secant
from .equation_systems.cholesky import Cholesky
from .equation_systems.crout import Crout
from .equation_systems.doolittle import Doolittle
from .equation_systems.gauss_elim_partial_pivot import GaussEliminationPartialPivot
from .equation_systems.gauss_elim_total_pivot import GaussEliminationTotalPivot
from .equation_systems.gauss_simple_elim import GaussEliminationSimple
from .equation_systems.gauss_factorization import GaussFactorization
from .equation_systems.gauss_factorization_pivot import GaussFactorizationPivot
from .equation_systems.jacobi import Jacobi
from .equation_systems.seidel import Seidel
from .equation_systems.sor import SOR
from .interpolation.newton import NewtonInterpolation
from .interpolation.lagrange import Lagrange
from .interpolation.vandermonde import Vandermonde
from .interpolation.linear_spline import LinearSpline
from .interpolation.cuadratic_spline import CuadraticSpline
from .interpolation.cubic_spline import CubicSpline

def createMethod(method):
    method = method.lower()

    if method == "inc_search":
        return IncrementalSearch()
    elif method == "bisection":
        return Bisection()
    elif method == "false_position":
        return FalsePosition()
    elif method == "fixed_point":
        return FixedPoint()
    elif method == "newton":
        return Newton()
    elif method == "multiple_roots":
        return MultipleRoots()
    elif method == "secant":
        return Secant()

    elif method == "simple_elimination":
        return GaussEliminationSimple()
    elif method == "partial_pivot_elimination":
        return GaussEliminationPartialPivot()
    elif method == "total_pivot_elimination":
        return GaussEliminationTotalPivot()

    elif method == "simple_factorization":
        return GaussFactorization()
    elif method == "partial_pivot_factorization":
        return GaussFactorizationPivot()
    elif method == "doolittle":
        return Doolittle()
    elif method == "crout":
        return Crout()
    elif method == "cholesky":
        return Cholesky()
    elif method == "jacobi":
        return Jacobi()
    elif method == "seidel":
        return Seidel()
    elif method == "sor":
        return SOR()

    elif method == "vandermonde":
        return Vandermonde()
    elif method == "newton_interpolation":
        return NewtonInterpolation()
    elif method == "lagrange":
        return Lagrange()
    elif method == "linear_spline":
        return LinearSpline()
    elif method == "cuadratic_spline":
        return CuadraticSpline()
    elif method == "cubic_spline":
        return CubicSpline()
    else:
        return NumericalMethod()
