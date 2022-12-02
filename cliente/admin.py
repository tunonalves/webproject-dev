from django.contrib import admin
from .models import cliente
# Register your models here.


class clienteadmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuit', 'direccion', 'telefono', 'email')
    search_fields = ('cuit', 'nombre',)
    list_filter = ('cuit','nombre',)
    readonly_fields = ('created', 'updated')


admin.site.register(cliente, clienteadmin)
