from django.urls import path
from .views import resta, info, index, ejer

urlpatterns = [
    path('', resta, name='resta'),
    path('info/', info, name='resta_info'),
    path('index/', index, name='resta_index'),
    path('ejer/', ejer, name='resta_ejer'),
    
] 
