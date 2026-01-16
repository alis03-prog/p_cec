from django.urls import path
from .views import rectas, info, index

urlpatterns = [
    path('', rectas, name='rectas'),
    path('info/', info, name='rectas_info'),
    path('index/', index, name='rectas_index'),
]
