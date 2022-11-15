from django import forms
from django.shortcuts import redirect, render

from blog.forms import *
from blog.models import *

# Create your views here.


def blog_inicio (request):
    recetas = Receta.objects.all()
    return render (request,'blog/index.html', {"recetas":recetas})

def blog_about (request):
    return render (request,'blog/about.html')

############ Start Crear Usuario ################
def blog_crear_usuario(request):
    if request.method == 'POST':
        form_user= FormCrearUsuario(request.POST)  
        if form_user.is_valid():
            data = form_user.cleaned_data
            if User.objects.filter(email__icontains = data['email']):
                return render (request,'blog/error_existe_en_db.html', { "dato" : data['email'] })
            else:
                user = User (nombre = data['nombre'], apellido = data['apellido'], email = data['email'] )
                user.save()
    form_user = FormCrearUsuario()
    return render (request,'blog/crear_usuario.html', {'form_user':form_user} )

############ END Crear User ################

############ Start ContactME Ingrdiente ################
def blog_contacto (request):
        if request.method == 'POST':
            form_contacto = FormCrearContactMe (request.POST)  
            if form_contacto.is_valid():
                 data = form_contacto.cleaned_data
                 print(data)
                 mensaje = ContactMe (usuario = data['usuario'], mensaje = data['mensaje'] )
                 mensaje.save()
        form_contacto  = FormCrearContactMe()
        return render (request,'blog/contact.html',{'form_contacto':form_contacto})
############ END ContactME Ingrdiente ################


############ Start Crear Ingrdiente ################

def blog_crear_ingrediente (request):
    if request.method == 'POST':
        form_ingrediente = FormCrearIngrediente (request.POST)  
        if form_ingrediente .is_valid():
            data = form_ingrediente.cleaned_data
            if Ingrediente.objects.filter(nombre__icontains = data['nombre']):
                return render (request,'blog/error_existe_en_db.html', { "dato" : data['nombre'] })
            else:
                user = Ingrediente (nombre = data['nombre'] )
                user.save()
    form_ingrediente  = FormCrearIngrediente()
    return render (request,'blog/crear_ingrediente.html', {'form_ingrediente':form_ingrediente } )
############ END Crear Ingrdiente ################


############ Start Crear Post ################

def blog_crear_post (request): 
    if request.method == 'POST':
        form_receta = FormCrearReceta(request.POST)  
        if form_receta.is_valid():
            data = form_receta.cleaned_data
            receta = Receta (titulo = data ['titulo'], proceso = data['proceso'], creador = data['creador'] )
            receta.save()
            list_ingredeintes = data['ingredientes']
            for ingrediente in list_ingredeintes:
                receta.ingrediente.add(ingrediente)
            receta.save()
    form_receta = FormCrearReceta()
    return render (request,'blog/crear_post.html', {'form_receta':form_receta} )
############ END Crear Post ################

############ Start Buscar Post ################
def blog_buscar (request):
    if request.method == 'POST':
        buscar = request.POST['buscar']
        if Receta.objects.filter(titulo__icontains = buscar):
            recetas = Receta.objects.filter(titulo__icontains = buscar)
            ingredientes = {''}
            for receta in recetas.all():
                ingredientes = receta.ingrediente.all()
            return render(request, "blog/buscar.html", {'buscar':buscar, 'recetas': recetas, 'ingredientes':ingredientes})
        else:
            return render (request,'blog/error_busqueda.html', { "dato" : buscar })

    return render(request, "blog/buscar.html", {})
############ END Buscar Post ################