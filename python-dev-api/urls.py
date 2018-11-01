from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("eval/", views.eval_function, name="evaluator"),
    path("plot/", views.plot, name="plot"),
    path("<str:method_name>/", views.call_method, name='invocar_metodo'),
]
