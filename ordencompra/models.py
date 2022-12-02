from django.db import models
from empresa.models import empresa
from cliente.models import cliente

# Create your models here.


class ordencompra(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cuit_empresa = models.ForeignKey(empresa, on_delete=models.CASCADE, verbose_name='CUIT Empresa')
    cuit_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, verbose_name='CUIT Cliente')
    descripcion = models.TextField(max_length=300, blank=False, null=False)
    numero_oc = models.CharField(max_length=30, blank=False, null=False, verbose_name='Nº de Orden de Compra')
    fecha_inicio = models.DateField(blank=False, null=False)
    fecha_fin = models.DateField(blank=False, null=False)
    importe = models.FloatField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ordencompra"
        verbose_name_plural = "ordenescompras"

    def __str__(self):
        texto = '{0}'
        return texto.format(self.numero_oc)
