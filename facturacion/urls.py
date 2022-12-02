from django.urls import path
from . import views

urlpatterns = [
    path('', views.facturalist.as_view(), name='facturacion'),
    path('facturacionADD/',views.facturaCreacion.as_view(),name='add_facturacion'),
    path('facturacionUPDATE/<pk>',views.facturaEdicion.as_view(),name='update_facturacion'),
    path('facturacionDELETE/<pk>',views.facturaEliminacion.as_view(),name='delete_facturacion'),
    path('facturacionDETAIL/<pk>',views.facturaDetalle.as_view(),name='detail_facturacion'),
]
