from django.urls import path
from .views import division, info, index, ejer

urlpatterns = [
    path('', division, name='division'),
    path('info/', info, name='division_info'),
    path('index/', index, name='division_index'),
    path('ejer/', ejer, name='division_ejer'),
]
