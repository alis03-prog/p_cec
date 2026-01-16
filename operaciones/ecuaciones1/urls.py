from django.urls import path
from .views import ecuaciones1, info, index

urlpatterns = [
    path('', ecuaciones1, name='ecuaciones1'),
    path('info/', info, name='ecuaciones1_info'),
    path('index/', index, name='ecuaciones1_index'),
]
