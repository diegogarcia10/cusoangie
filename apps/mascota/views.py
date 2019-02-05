from django.shortcuts import render,redirect
from django.http import HttpResponse
#vistas basadas en clases
from django.urls import reverse_lazy# ha sido movido de esta clase django.core.urlresolvers hoy esta en la que esta xD
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
	
# Create your views here.
#VISTAS BASADAS EN METODOS
def index(request):
	return render(request,'mascota/index.html')

def mascota_view(request):
	if request.method=='POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	else:
		form=MascotaForm()
	return render(request,'mascota/mascota_form.html',{'form':form})
	pass

def mascota_list(request):
	mascota=Mascota.objects.all().order_by("folio")
	contexto={'mascotas' :mascota }
	return render(request,'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(folio=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_form.html', {'form':form})
def mascota_delete(request,id_mascota):
	mascota = Mascota.objects.get(folio=id_mascota)
	if request.method=='POST':
		mascota.delete()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})
#VISTAS BASADAS EN CLASES
class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota/mascota_list.html'

class MascotaCreate(CreateView):
	model=Mascota 
	form_class = MascotaForm
	template_name='mascota/mascota_form.html'
	success_url=reverse_lazy('mascota:mascota_listar')

class MascotaUpdate(UpdateView):
	model=Mascota
	form_class = MascotaForm
	template_name='mascota/mascota_form.html'
	success_url=reverse_lazy('mascota:mascota_listar')

class MascotaDelete(DeleteView):
	model=Mascota
	template_name='mascota/mascota_delete.html'
	success_url=reverse_lazy('mascota:mascota_listar')
		