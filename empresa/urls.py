from django.urls import path
from . import views

urlpatterns = [
    path('',views.empresalist.as_view(),name='empresas'),
    path('empresaADD/',views.empresaCreacion.as_view(),name='add_empresa'),
    path('empresaUPDATE/<pk>',views.empresaEdicion.as_view(),name='update_empresa'),
    path('empresaDELETE/<pk>',views.empresaEliminacion.as_view(),name='delete_empresa'),
    path('empresaDETAIL/<pk>',views.empresaDetalle.as_view(),name='detail_empresa'),
]