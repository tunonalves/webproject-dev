from django import forms
from .models import pagos

class formPagos(forms.ModelForm):
    class Meta:
        model = pagos
        fields = '__all__'
