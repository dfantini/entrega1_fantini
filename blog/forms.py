from django import forms 
from blog.models import *


class FormCrearUsuario (forms.Form):
    nombre = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=50,required=False,widget=forms.EmailInput(attrs={'class':'form-control'}))


class FormCrearIngrediente (forms.Form):
    nombre = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    

class FormCrearReceta (forms.Form):
    creador = forms.ModelChoiceField(queryset=User.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'})) 
    titulo = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    ingredientes = forms.ModelMultipleChoiceField(queryset=Ingrediente.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class':'form-floating'}),required=False )
    proceso = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'height: 12rem'}),required=False)

  
  
class FormCrearContactMe (forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'height: 12rem'}),required=False)

