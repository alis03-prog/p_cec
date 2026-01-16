
from django.contrib import admin
from django.urls import  include, path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('suma/', include('suma.urls')),
    path('resta/', include('resta.urls')), 
    path('multiplicacion/', include('multiplicacion.urls')),
    path('division/', include('division.urls')),
    path('factorizacion/', include('factorizacion.urls')),
    path('jerarquia/', include('jerarquia.urls')),
    path('polinomios/', include('polinomios.urls')),
    path('rectas/', include('rectas.urls')),
    path('ecuaciones1/', include('ecuaciones1.urls')),
    path('ecuaciones2/', include('ecuaciones2.urls')),
    path('perimetros/', include('perimetros.urls')),
    path('areas/', include('areas.urls')), 
]
 