from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import ordencompra
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import formOrdenCompras
# Create your views here.


def ordencompras(request):
    return render(request, 'ordencompra.html')


class ordenlist(ListView):
    model = ordencompra
    template_name = 'ordencompra.html'

class ordencomprasDetalle(DetailView):
    model = ordencompra
    template_name = "detail_ordencompra.html"
    
class ordencomprasCreacion(CreateView):
    model = ordencompra
    form_class = formOrdenCompras
    template_name = 'add_ordencompra.html'
    success_url = reverse_lazy("ordencompras")  

class ordencomprasEdicion(UpdateView):
    model = ordencompra
    template_name = 'update_ordencompra.html'
    success_url = reverse_lazy("ordencompras")  
    fields = "__all__"

class ordencomprasEliminacion(DeleteView):
    model = ordencompra
    template_name = 'delete_ordencompra.html'
    success_url = reverse_lazy("ordencompras")  