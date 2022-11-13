from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def blog_inicio (request):
    return render (request,'blog/index.html')

def blog_about (request):
    return render (request,'blog/about.html')

def blog_post (request):
    return render (request,'blog/post.html')

def blog_sing_up (request):
    return render (request,'blog/singup.html')

def blog_contact (request):
    return render (request,'blog/contact.html')