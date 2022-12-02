from django.db import models
from facturacion.models import facturacion

# Create your models here.


class pagos(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    numero_factura = models.ForeignKey(
        facturacion, related_name='facpagos', on_delete=models.CASCADE, verbose_name='Nª de Factura')
    fecha = models.DateField(blank=False, null=False)
    importe = models.FloatField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "pago"
        verbose_name_plural = "pagos"

    def __str__(self):
        texto = '{0}'
        return texto.format(self.numero_factura)
