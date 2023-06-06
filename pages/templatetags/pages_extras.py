from django import template
from pages.models import Page

register = template.Library() 

@register.simple_tag #Transforma una funcion normal en un tag simple y se registra en la libreria de templates
def get_page_list():
    pages = Page.objects.all()  #Recupera todas las páginas
    return pages