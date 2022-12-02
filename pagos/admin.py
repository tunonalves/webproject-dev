from django.contrib import admin
from .models import pagos
# Register your models here.


class pagosadmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'fecha', 'importe')
    search_fields = ('numero_factura', 'fecha', 'importe')
    list_filter = ('numero_factura', 'fecha', 'importe',)
    date_hierarchy = ('fecha')
    readonly_fields = ('created', 'updated')


admin.site.register(pagos, pagosadmin)
