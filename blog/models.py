from django.db import models
from django.utils.timezone import now #Detecta zona horaria en la qué está configurado el proyecto

from ckeditor.fields import RichTextField #Importando el editor WYSIWYG

from django.contrib.auth.models import User 
# User es el modelo que gestiona Django con los usuarios que se crean en el panel del administrador y/o usuarios que se gestionan con la autenticación y el registro

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['created']

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nombre")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now) #Forma que prefiere Django 
    #image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True) #Es necesaria la imagen para el html
    author = models.ForeignKey(User, verbose_name="Nombre del autor", on_delete=models.CASCADE) #CASCADE borra      todas las entradas que tenía el autor - PROTECT(Evita borrar las entradas al borrar el usuario)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['created']

    def __str__(self):
        return self.title