from django.db import models

# Create your models here.

class Users (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

class Ingredientes (models.Model):
    nombre = models.CharField(max_length=100)

class Receta (models.Model):
    titulo = models.CharField(max_length=100)
    proceso = models.TextField()
    ingrediente = models.ManyToManyField(Ingredientes)
    cantidades = models.CharField(max_length=100)
    creador = models.ForeignKey(Users, on_delete=models.CASCADE)
    

class ContactMe (models.Model):
    usuario = models.ForeignKey(Users, on_delete=models.CASCADE)
    mensaje = models.TextField()


