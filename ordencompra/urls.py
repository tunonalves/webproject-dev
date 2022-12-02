from django.urls import path
from . import views

urlpatterns = [
    path('',views.ordenlist.as_view(),name='ordencompras'),
    path('ordencomprasADD/',views.ordencomprasCreacion.as_view(),name='add_ordencompras'),
    path('ordencomprasUPDATE/<pk>',views.ordencomprasEdicion.as_view(),name='update_ordencompras'),
    path('ordencomprasDELETE/<pk>',views.ordencomprasEliminacion.as_view(),name='delete_ordencompras'),
    path('ordencomprasDETAIL/<pk>',views.ordencomprasDetalle.as_view(),name='detail_ordencompras'),
]