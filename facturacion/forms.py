from django import forms
from .models import facturacion

class formFacturacion(forms.ModelForm):
    class Meta:
        model = facturacion
        fields = '__all__'
