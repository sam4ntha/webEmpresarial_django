from django.contrib import admin
from .models import Category, Post #Crear administrador para el blog

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories') 
    ordering = ('author', 'published')
    search_fields = ('title','content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

# ordering es para las columnas que se quieren mostrar
# guiones bajos indican que se va a buscar de los modelos relacionados (ManyToMany)
# date_hierarchy es para jerarquizar las entradas por fechas de publicación
# list_filter se le pasan campos para que los filtre


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)