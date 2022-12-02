from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import cliente
from .forms import formCliente

# Create your views here.


def clientes(request):
    return render(request, 'cliente.html')


class clientelist(ListView):
    model = cliente
    template_name = 'cliente.html'

class clienteDetalle(DetailView):
    model = cliente
    form_class = formCliente
    template_name = "detail_cliente.html"


class clienteCreacion(CreateView):
    model = cliente
    form_class = formCliente
    template_name = 'add_cliente.html'
    success_url = reverse_lazy("cliente")  


class clienteEdicion(UpdateView):
    model = cliente
    template_name = 'update_cliente.html'
    success_url = reverse_lazy("cliente")
    fields = "__all__" 
 


class clientetEliminacion(DeleteView):
    model = cliente
    template_name = 'delete_cliente.html'
    success_url = reverse_lazy("cliente")  

