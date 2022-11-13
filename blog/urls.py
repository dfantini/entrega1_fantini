from django.urls import path
from  blog import views

urlpatterns = [
    path ( '', views.blog_inicio , name = 'blog-inicio'),
    path ( 'about/', views.blog_about , name = 'blog-about'),
    path ( 'post/', views.blog_post, name = 'blog-post'),
    path ( 'singup/', views.blog_sing_up , name = 'blog-singup'),
    path ( 'contact/', views.blog_contact , name = 'blog-contact'),
]
