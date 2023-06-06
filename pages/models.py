from django.db import models
from ckeditor.fields import RichTextField #Importando el editor WYSIWYG

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido") #Sustituimos a models.TextField
    order = models.SmallIntegerField(default=0 ,verbose_name="Orden")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title