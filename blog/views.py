from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Users, Ingredientes, Receta, ContactMe

# Create your views here.


def blog_inicio (request):
    recetas = Receta.objects.all()
    return render (request,'blog/index.html', {'recetas' : recetas})

def blog_about (request):
    return render (request,'blog/about.html')

def blog_post (request):
    return render (request,'blog/post.html')

### Es para crear users en la BDD
def blog_sing_up (request):
    if request.method == "POST":
        nombre_usuario = request.POST['nombre']
        apellido_usuario = request.POST['apellido']
        email_usuario = request.POST['email']
        user = Users ( nombre = nombre_usuario, apellido = apellido_usuario, email = email_usuario)
        user.save()
    return render (request,'blog/singup.html')
############ END Crear User ################

def blog_contact (request):
    return render (request,'blog/contact.html')


############ Start Crear Ingrdiente ################

def blog_crear_ingrediente (request):
        if request.method == "POST":
            ingrediente_ingresado = request.POST["ingrediente"]
            if Ingredientes.objects.filter(nombre__icontains = ingrediente_ingresado):
                return render (request,'blog/error_existe_en_db.html', { "dato" : ingrediente_ingresado })
            else:
                ingrediente = Ingredientes ( nombre = ingrediente_ingresado)
                ingrediente.save()
        return render (request,'blog/crear_ingrediente.html')
    

############ END Crear Ingrdiente ################

############ Start Crear Post ################

def blog_crear_post (request):
            return render (request,'blog/crear_ingrediente.html')


    

############ END Crear Post ################
