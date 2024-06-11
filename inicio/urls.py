from django.urls import path
from .views import inicio, peliculas

urlpatterns = [
    path('',inicio),
    path('/peliculas',peliculas,name='peliculas'),
    
    
    
]