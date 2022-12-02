from django import forms
from .models import empresa

class formEmpresa(forms.ModelForm):
    class Meta:
        model = empresa
        fields = '__all__'
