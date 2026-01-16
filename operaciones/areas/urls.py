from django.urls import path
from .views import areas, info, index

urlpatterns = [
    path('', areas, name='areas'),
    path('info/', info, name='areas_info'),
    path('index/', index, name='areas_index'),
]
