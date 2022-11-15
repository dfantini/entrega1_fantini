from django.urls import path
from  blog import views

urlpatterns = [
    path ( '', views.blog_inicio , name = 'blog-inicio'),
    path ( 'crear-ingrediente/', views.blog_crear_ingrediente, name = 'blog-post-crear-ingrediente'),
    path ( 'crear-post/', views.blog_crear_post, name = 'blog-post-crear-post'),
    path ( 'crear-usuario/', views.blog_crear_usuario , name = 'blog-crear-usuario'),
    path ( 'contact/', views.blog_contacto , name = 'blog-contact'),
    path ( 'buscar/', views.blog_buscar , name = 'blog-buscar'),

]
