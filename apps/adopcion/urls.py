#from django.urls import path
from django.conf.urls import url,include
from apps.adopcion.views import SolicitudList, SolicitudCreate, SolicitudUpdate,\
SolicitudDelete
app_name="adopcion"

urlpatterns = [
  url(r'solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
  url(r'solicitud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
  url(r'solicitud/editar/(?P<pk>\d+)', SolicitudUpdate.as_view(), name = 'solicitud_editar'),
  url(r'solicitud/eliminar/(?P<pk>\d+)', SolicitudDelete.as_view(),name = 'solicitud_eliminar'),
]