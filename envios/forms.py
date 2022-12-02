from django import forms
from .models import envio

class formEnvio(forms.ModelForm):
    class Meta:
        model = envio
        fields = '__all__'
