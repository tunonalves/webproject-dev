from django import forms
from .models import ordencompra

class formOrdenCompras(forms.ModelForm):
    class Meta:
        model = ordencompra
        fields = '__all__'
