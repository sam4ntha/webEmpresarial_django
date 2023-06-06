#Importar urls de forma práctica, extendiendose de forma más cómoda las apps
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact')
]