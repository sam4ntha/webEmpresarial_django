from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(max_length=100, unique=True, verbose_name="Nombre clave")
    name = models.CharField(max_length=200, verbose_name="Red social")
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name="Enlace")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name