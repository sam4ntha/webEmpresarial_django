from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/terms.html', {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id) #forma elegante de mostrar que no existe esa búsqueda
    #category = Category.objects.get(id=category_id) #get permite recoger un único reistro filtrando por una serie de campos (id)
    #posts = Post.objects.filter(categories=category) #categoría que se ha recuperado antes
    return render(request, "blog/category.html", {'category':category})