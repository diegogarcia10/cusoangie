from django.shortcuts import render

# Create your views here.
#importaremos modelos que trae ya django para los user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
#vistas basadas en clases
from django.urls import reverse_lazy# ha sido 
#movido de esta clase django.core.urlresolvers hoy esta en la que esta xD
from apps.usuario.forms import RegistroForm
class RegistroUsuario(CreateView):
	model=User
	template_name='usuario/registrar.html'
	form_class=RegistroForm
	success_url=reverse_lazy('mascota:mascota_listar')
