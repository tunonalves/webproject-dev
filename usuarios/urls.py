from django.urls import path
from . import views

urlpatterns = [
    path('',views.usuarios,name='usuarios'),
    path('registro/',views.Vregistro.as_view(),name='registro')
]