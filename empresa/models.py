from django.db import models

# Create your models here.


class empresa(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cuit = models.IntegerField(unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "empresa"
        verbose_name_plural = "empresas"

    def __str__(self):
        texto = '{0}'
        return texto.format(self.nombre)
