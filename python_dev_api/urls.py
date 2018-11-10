from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("eval/", views.evalFunction, name="evaluator"),
    path("plot/", views.plotFunction, name="plot"),
    path("<str:method_name>/", views.methodService, name='invocar_metodo'),
]
