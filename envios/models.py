from django.db import models
from facturacion.models import facturacion
from ordencompra.models import ordencompra

# Create your models here.


class envio(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    Numero_Factura = models.ForeignKey(facturacion, related_name='facenvios', on_delete=models.CASCADE, verbose_name='Nº de Factura')
    Numero_OC = models.ForeignKey(ordencompra, on_delete=models.CASCADE, verbose_name='Nº de Orden de Compra')
    Fecha_envio = models.DateField(blank=False, verbose_name='Fecha de Envio', null=False)
    Fecha_recepcion = models.DateField(blank=True, verbose_name='Fecha de Recepcion', null=False)
    Email_enviado = models.EmailField(max_length=254, blank=False, verbose_name='Email Enviado', null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "envio"
        verbose_name_plural = "envios"

    def __str__(self):
        texto = '{0}'
        return texto.format(self.Numero_Factura.cuit_empresa.nombre)
