from django.urls import path
from .views import perimetros, info, index

urlpatterns = [
    path('', perimetros, name='perimetros'),
    path('info/', info, name='perimetros_info'),
    path('index/', index, name='perimetros_index'),
]
