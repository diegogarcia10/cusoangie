#from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required

from apps.mascota.views import index, mascota_view,mascota_list,mascota_edit,mascota_delete, MascotaList,MascotaCreate,\
MascotaUpdate,MascotaDelete
app_name="mascota"
urlpatterns = [
    #path(r'', index, name='index'),
    #path(r'nuevo/', mascota_view, name='mascota_crear'),
    #path(r'listar/', mascota_list , name='mascota_listar'),
    #path(r'editar/(?P<id_mascota>)/', mascota_edit , name='mascota_editar'),
    url(r'^$', index, name='index'),
    url(r'nuevo',login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'listar',login_required(MascotaList.as_view()), name='mascota_listar'),
	url(r'editar/(?P<pk>\d+)/',login_required(MascotaUpdate.as_view()), name='mascota_editar'),
	url(r'eliminar/(?P<pk>\d+)/',login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
]