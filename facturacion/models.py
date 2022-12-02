from django.db import models
from empresa.models import empresa
from cliente.models import cliente
from ordencompra.models import ordencompra

# Create your models here.


class facturacion(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cuit_empresa = models.ForeignKey(empresa, on_delete=models.CASCADE, verbose_name='CUIT Empresa')
    cuit_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, verbose_name='CUIT Cliente')
    numero_oc = models.ForeignKey(ordencompra, on_delete=models.CASCADE, verbose_name='Nº de Orden de Compra')
    descripcion = models.TextField(max_length=300, blank=False, null=False)
    numero_factura = models.CharField(max_length=30, blank=False, null=False, verbose_name='Nº de Factura')
    fecha = models.DateField(blank=False, null=False)
    importe = models.FloatField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "factura"
        verbose_name_plural = "facturas"

    def __str__(self):
        texto = '{0}'
        return texto.format(self.numero_factura)
