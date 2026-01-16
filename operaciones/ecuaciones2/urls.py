from django.urls import path
from .views import ecuaciones2, info, index

urlpatterns = [
    path('', ecuaciones2, name='ecuaciones2'),
    path('info/', info, name='ecuaciones2_info'),
    path('index/', index, name='ecuaciones2_index'),
]
