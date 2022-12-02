from django import forms
from .models import cliente

class formCliente(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'