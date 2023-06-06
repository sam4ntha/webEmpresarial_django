#Importar urls de forma práctica, extendiendose de forma más cómoda las apps
from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page') #<>Detecta cadena de caracteres - convertir a el tipo de valor que se desea agregar
]