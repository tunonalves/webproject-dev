from django.urls import path
from . import views

urlpatterns = [
    path('',views.enviolist.as_view(),name='envios'),
    path('envioADD/',views.envioCreacion.as_view(),name='add_envio'),
    path('envioUPDATE/<pk>',views.envioEdicion.as_view(),name='update_envio'),
    path('envioDELETE/<pk>',views.envioEliminacion.as_view(),name='delete_envio'),
    path('envioDETAIL/<pk>',views.envioDetalle.as_view(),name='detail_envio'),
]