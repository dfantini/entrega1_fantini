from django.db import models

# Create your models here.

class User (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.email

class Ingrediente (models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Receta (models.Model):
    titulo = models.CharField(max_length=100)
    proceso = models.TextField()
    ingrediente = models.ManyToManyField(Ingrediente)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

class ContactMe (models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()


