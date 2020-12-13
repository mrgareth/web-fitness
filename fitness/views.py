from django.shortcuts import render

from django.views.generic import ListView, DetailView  
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .models import Usuario

from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

# Create your views here.
class UsuarioList(ListView):
    model = Usuario

class UsuarioCreate(SuccessMessageMixin, CreateView): 
    model = Usuario
    form = Usuario
    fields = "__all__"
    success_message = 'Usuario Creado Correctamente !' 
    
    def get_success_url(self):        
        return reverse('usuarios')

class UsuarioDetail(DetailView):
    model = Usuario

class UsuarioUpdate(SuccessMessageMixin, UpdateView): 
    model = Usuario  
    form = Usuario 
    fields = "__all__"  
    success_message = 'Usuario Actualizado Correctamente !' 
 
    def get_success_url(self):               
        return reverse('usuarios')

class UsuarioClear(SuccessMessageMixin, DeleteView): 
    model = Usuario 
    form = Usuario
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Usuario Eliminado Correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('usuarios')

def register(request, *args, **kwargs):
    return render(request, "fitness/register.html", {})

def pesos(request, *args, **kwargs):
    return render(request, "fitness/pesosLineChart.html", {})

def ejercicio(request, *args, **kwargs):
    return render(request, "fitness/BarChart.html", {})
    
def calorias(request):
    return render(request, "fitness/calorias.html", {})
