from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import envio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import formEnvio

# Create your views here.
def envios(request):
    return render(request,'envios.html')

class enviolist(ListView):
    model = envio
    template_name = 'envios.html'

class envioDetalle(DetailView):
    model = envio
    template_name = "detail_envio.html"
    
class envioCreacion(CreateView):
    model = envio
    form_class = formEnvio
    template_name = 'add_envio.html'
    success_url = reverse_lazy("envios")  

class envioEdicion(UpdateView):
    model = envio
    template_name = 'update_envio.html'
    success_url = reverse_lazy("envios")  
    fields = "__all__"

class envioEliminacion(DeleteView):
    model = envio
    template_name = 'delete_envio.html'
    success_url = reverse_lazy("envios")  