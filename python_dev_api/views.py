from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from sympy import SympifyError

from .numerical_methods.method_factory import createMethod
from .numerical_methods.one_variable_equations.one_variable_equations_parent import call_eval_function, plot_function
import json

def index(request):
    return JsonResponse({"test": "Hello world"})

@csrf_exempt
def methodService(request, method_name):
    try:
        method = createMethod(method_name)
        if request.method == 'GET':
            return JsonResponse({'help': method.getHelp()})
        else:
            params = json.loads(request.body.decode('UTF-8'))
            return JsonResponse(method.evaluate(params))
    except SympifyError as e:
        return JsonResponse({'error': 'Invalid Input'})
    except KeyError as e:
        return JsonResponse({'error': str(e)})


@csrf_exempt
def evalFunction(request):
    params = json.loads(request.body.decode('UTF-8'))
    return JsonResponse(call_eval_function(params))


@csrf_exempt
def plotFunction(request):
    params = json.loads(request.body.decode('UTF-8'))
    return JsonResponse(plot_function(params))
