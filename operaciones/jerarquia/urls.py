from django.urls import path
from .views import jerarquia, info, index

urlpatterns = [
    path('', jerarquia, name='jerarquia'),
    path('info/', info, name='jerarquia_info'),
    path('index/', index, name='jerarquia_index'),
]
