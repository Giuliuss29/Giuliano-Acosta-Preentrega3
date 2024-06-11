from django.urls import path
from .views import inicio, peliculas, series, famosos

urlpatterns = [
    path('',inicio),
    path('/peliculas',peliculas,name='peliculas'),
    path('/series',series,name='series'),
    path('/famosos',famosos,name='famosos')
    
    
    
]