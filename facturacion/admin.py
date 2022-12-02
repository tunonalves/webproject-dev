from django.contrib import admin
from .models import facturacion
# Register your models here.


class facturacionadmin(admin.ModelAdmin):
    list_display = ('cuit_cliente', 'cuit_empresa', 'numero_oc',
                    'numero_factura', 'importe', 'fecha', 'descripcion')
    search_fields = ('numero_factura',)
    list_filter = ('importe', 'fecha',)
    date_hierarchy = ('fecha')
    readonly_fields = ('created', 'updated')


admin.site.register(facturacion, facturacionadmin)
