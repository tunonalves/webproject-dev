from django.db import models

# Create your models here.


class cliente(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cuit = models.IntegerField(unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False, null=False)
    telefono = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        texto = '{0}'
        return texto.format(self.nombre)
