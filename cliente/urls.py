from django.urls import path
from . import views

urlpatterns = [
    path('',views.clientelist.as_view(),name='cliente'),
    path('clienteADD/',views.clienteCreacion.as_view(),name='add_cliente'),
    path('clienteUPDATE/<pk>',views.clienteEdicion.as_view(),name='update_cliente'),
    path('clienteDELETE/<pk>',views.clientetEliminacion.as_view(),name='delete_cliente'),
    path('clienteDETAIL/<pk>',views.clienteDetalle.as_view(),name='detail_cliente'),
]