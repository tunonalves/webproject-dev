from django.contrib import admin
from .models import ordencompra
# Register your models here.


class ocadmin(admin.ModelAdmin):
    list_display = ('cuit_cliente', 'cuit_empresa', 'numero_oc',
                    'fecha_inicio', 'fecha_fin', 'importe', 'descripcion')
    search_fields = ('cuit_cliente', 'cuit_empresa', 'numero_oc', 'importe')
    list_filter = ('numero_oc', 'cuit_cliente','cuit_empresa',)
    date_hierarchy = ('fecha_fin')
    readonly_fields = ('created', 'updated')


admin.site.register(ordencompra, ocadmin)
