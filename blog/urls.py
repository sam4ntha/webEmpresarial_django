#Importar urls de forma práctica, extendiendose de forma más cómoda las apps
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='terms'),
    path('category/<int:category_id>', views.category, name='category'), #<>Detecta cadena de caracteres - convertir a el tipo de valor que se desea agregar
]