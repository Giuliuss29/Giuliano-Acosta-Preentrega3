from django.shortcuts import render
from inicio.forms import FormPelicula, FormSeries, FormFamosos

def inicio(request):
    return render(request,'index.html' )

def peliculas(request):
    return render(request,'peliculas.html' )
    
    if datos.method == 'POST':
        formulario = FormPelicula(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            pelicula = Peliucla(titulo=datos.POST.get('titulo'), director=datos.POST.GET('director'), genero=datos.POST.GET('genero'))
            pelicula.save
    formulario = FormPelicula()
    return render(request,'inicio/peliculas.html',{'formulario':formulario})        


def series(request):
    return render(request,'series.html')
    
    if datos.method == 'POST':
        formulario = FormSeries(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            series = Serie(titulo=datos.POST.get('titulo'), director=datos.POST.GET('director'), genero=datos.POST.GET('genero'), temporadas=datos.Post.get('temporadas'))
            series.save
    formulario = FormSeries()
    return render(request,'inicio/series.html',{'formulario':formulario}) 


def famosos(request):
    return render(request,'famosos.html')

    if datos.method == 'POST':
        formulario = FormFamosos(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            famosos = Famosos(nombre=datos.POST.get('nombre'), profesion=datos.POST.GET('profesion'))
            famosos.save
    formulario = FormFamosos()
    return render(request,'inicio/famosos.html',{'formulario':formulario}) 
    
