from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import pagos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import formPagos
# Create your views here.


def pago(request):
    return render(request, 'pagos.html')

class pagosList(ListView):
    model = pagos
    template_name = 'pagos.html'

class pagosDetalle(DetailView):
    model = pagos
    template_name = "detail_pagos.html"
    
class pagosCreacion(CreateView):
    model = pagos
    form_class = formPagos
    template_name = 'add_pagos.html'
    success_url = reverse_lazy("pagos")  

class pagosEdicion(UpdateView):
    model = pagos
    template_name = 'update_pagos.html'
    success_url = reverse_lazy("pagos")  
    fields = "__all__"

class pagosEliminacion(DeleteView):
    model = pagos
    template_name = 'delete_pagos.html'
    success_url = reverse_lazy("pagos")  