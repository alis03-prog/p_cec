from django.urls import path
from .views import suma, info, index, ejer

urlpatterns = [
    path('', suma, name='suma'),
    path('info/', info, name='suma_info'),
    path('index/', index, name='suma_index'),
    path('ejer/', ejer, name='suma_ejer'),
]
