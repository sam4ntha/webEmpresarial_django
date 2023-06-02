from django.contrib import admin
from .models import Service

# Register your models here. -ServiceAdmin solo lectura las fechas
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
