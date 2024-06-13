from django.shortcuts import render, redirect
from inicio.forms import FormPelicula, FormSeries, FormFamosos
from inicio.models import Peliculas, Series, Famosos


def inicio(request):
    return render(request,'index.html' )

def peliculas(request):
    
    if request.method == 'POST':
        formulario = FormPelicula(request.POST,request.FILES)
        if formulario.is_valid():
            pelicula=formulario.save(commit=False)
            pelicula.save()
            return redirect('inicio')
    else: 
        formulario=FormPelicula()
    return render(request,'peliculas.html',{'formulario':formulario})        
 
def series(request):
    
    if request.method == 'POST':
        formulario = FormSeries(request.POST,request.FILES)
        if formulario.is_valid():
            serie=formulario.save(commit=False)
            serie.save()
            return redirect('inicio')
    else: 
        formulario=FormSeries()
    return render(request,'series.html',{'formulario':formulario})  


def famosos(request):

    if request.method == 'POST':
        formulario = FormFamosos(request.POST,request.FILES)
        if formulario.is_valid():
            famosos=formulario.save(commit=False)
            famosos.save()
            return redirect('inicio')
    else: 
        formulario=FormFamosos()
    return render(request,'famosos.html',{'formulario':formulario}) 


def buscar(request):
    
    peliculas=[]
    series=[]
    famosos=[]
    
    if request.method=='POST':
       titulo_pelicula=request.POST.get('titulo_pelicula','')
       titulo_serie=request.POST.get('titulo_serie','')
       nombre_famoso=request.POST.get('nombre_famoso','')
    
       
    
       
       if titulo_pelicula:
            peliculas = Peliculas.objects.filter(titulo__icontains = titulo_pelicula)
       if titulo_serie:
           series = Series.objects.filter(titulo__icontains = titulo_serie)
       if nombre_famoso:
           famosos = Famosos.objects.filter(nombre__icontains = nombre_famoso)
       return render(request,'resultados.html',{ 
            'peliculas':peliculas,
            'series':series,
            'famosos':famosos})
    else:
        return render(request,'busqueda.html')         
           
       
       
    
       
    
