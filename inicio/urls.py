from django.urls import path
from .views import inicio, peliculas, series, famosos, buscar

urlpatterns = [
    path('',inicio,name='inicio'),
    path('peliculas/',peliculas,name='peliculas'),
    path('series/',series,name='series'),
    path('famosos/',famosos,name='famosos'),
    path('busqueda/',buscar,name='buscar'),
    
    
    
]