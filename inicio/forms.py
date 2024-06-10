from django import forms 
from inicio.models import Peliculas, Series, Famosos

class FormPelicula(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = ['titulo', 'director', 'genero']
        
class FormSeries(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['titulo', 'director', 'genero', 'temporadas'] 


class FormFamosos(forms.ModelForm):
    class Meta:
        model = Famosos
        fields = ['nombre', 'profesion']                   