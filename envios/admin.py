from django.contrib import admin
from .models import envio
# Register your models here.


class envioadmin(admin.ModelAdmin):
    list_display = ('Numero_Factura', 'Numero_OC', 'Fecha_envio',
                    'Fecha_recepcion', 'Email_enviado')
    search_fields = ('Numero_Factura', 'Numero_OC', 'Email_enviado',)
    list_filter = ('Numero_Factura', 'Fecha_envio', 'Numero_OC',)
    date_hierarchy = ('Fecha_envio')
    readonly_fields = ('created', 'updated')


admin.site.register(envio, envioadmin)
