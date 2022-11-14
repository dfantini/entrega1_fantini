from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Users, Ingredientes, Receta, ContactMe

# Create your views here.


def blog_inicio (request):
    recetas = Receta.objects.all()
    return render (request,'blog/index.html', {"recetas":recetas})

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

    users = Users.objects.all()
    ingredientes = Ingredientes.objects.all()

    contex = {
        "users":users,
        "ingrdientes":ingredientes
    }
       
    if request.method == "POST":
        titulo = request.POST["titulo"]
        user_mail = request.POST.get('user_email')
        for user in users:
            if user.email == user_mail:
                creador = Users.objects.get(id=user.id) 
        ingredientes = request.POST.get('ingrdientes_seleccionados')
        proceso = request.POST['proceso']
        post = Receta (titulo = titulo, proceso = proceso, creador = creador ) #, ingrediente =ingredientes,
        post.save()
    return render (request,'blog/crear_post.html', contex )
############ END Crear Post ################

############ Start Cargar Post ################
