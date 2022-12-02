from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import empresa
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import formEmpresa

# Create your views here.
def empresas(request):
    return render(request,'empresa.html')

class empresalist(ListView):
    model = empresa
    template_name = 'empresa.html'

class empresaDetalle(DetailView):
    model = empresa
    template_name = "detail_empresa.html"


class empresaCreacion(CreateView):
    model = empresa
    form_class = formEmpresa
    template_name = 'add_empresa.html'
    success_url = reverse_lazy("empresas")  


class empresaEdicion(UpdateView):
    model = empresa
    template_name = 'update_empresa.html'
    success_url = reverse_lazy("empresas")  
    fields = "__all__"


class empresaEliminacion(DeleteView):
    model = empresa
    template_name = 'delete_empresa.html'
    success_url = reverse_lazy("empresas")  
