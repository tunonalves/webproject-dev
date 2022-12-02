from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import facturacion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import formFacturacion


def facturaciones(request):
    return render(request, 'facturacion.html')


class facturalist(ListView):
    model = facturacion
    template_name = 'facturacion.html'

class facturaDetalle(DetailView):
    model = facturacion
    template_name = "detail_facturacion.html"


class facturaCreacion(CreateView):
    model = facturacion
    form_class = formFacturacion
    template_name = 'add_facturacion.html'
    success_url = reverse_lazy("facturacion")  


class facturaEdicion(UpdateView):
    model = facturacion
    template_name = 'update_facturacion.html'
    success_url = reverse_lazy("facturacion")  
    fields = "__all__"


class facturaEliminacion(DeleteView):
    model = facturacion
    template_name = 'delete_facturacion.html'
    success_url = reverse_lazy("facturacion")  
