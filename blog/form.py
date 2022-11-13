from django import forms 
from blog.models import Users, Ingredientes, Receta, ContactMe


class FormUserCrear (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class FormIngredienteCrear (forms.Form):
    nombre = forms.CharField()

class FormCrearReceta (forms.Model):
    titulo = forms.CharField(max_length=100)
    proceso = forms.TextField()
    ingrediente = forms.ManyToManyField()
    cantidades = forms.CharField(max_length=100)
    creador = forms.ModelChoiceField (queryset= Users.objectes.all())

    
class CrearContactMe (forms.Model):
    usuario = forms.ModelChoiceField (queryset= Users.objectes.all())
    mensaje = forms.TextField()

