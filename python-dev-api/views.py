from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from sympy import SympifyError

from .metodos.method_factory import create_method
from .metodos.ecuaciones_no_lineales.utils import call_eval_f
from .metodos.ecuaciones_no_lineales.utils import plot_f
import json

@csrf_exempt
def call_method(request, method_name):
    try:
        method = create_method(method_name)
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
    params = params = json.loads(request.body.decode('UTF-8'))
    return JsonResponse(evalFunction(params))


@csrf_exempt
def plotFunction(request):
    params = params = json.loads(request.body.decode('UTF-8'))
    return JsonResponse(plotFunction(params))
