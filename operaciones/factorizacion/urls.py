from django.urls import path
from .views import factorizacion, info, index

urlpatterns = [
    path('', factorizacion, name='factorizacion'),
    path('info/', info, name='factorizacion_info'),
    path('index/', index, name='factorizacion_index'),
]
