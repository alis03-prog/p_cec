from django.urls import path
from .views import multiplicacion, info, index, ejer

urlpatterns = [
    path('', multiplicacion, name='multiplicacion'),
    path('info/', info, name='multiplicacion_info'),
    path('index/', index, name='multiplicacion_index'),
    path('ejer/', ejer, name='multiplicacion_ejer'),
]
