from django.urls import path
from .views import polinomios, info, index

urlpatterns = [
    path('', polinomios, name='polinomios'),
    path('info/', info, name='polinomios_info'),
    path('index/', index, name='polinomios_index'),
]
