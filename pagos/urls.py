from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagosList.as_view(), name='pagos'),
    path('ordencomprasADD/',views.pagosCreacion.as_view(),name='add_pagos'),
    path('ordencomprasUPDATE/<pk>',views.pagosEdicion.as_view(),name='update_pagos'),
    path('ordencomprasDELETE/<pk>',views.pagosEliminacion.as_view(),name='delete_pagos'),
    path('ordencomprasDETAIL/<pk>',views.pagosDetalle.as_view(),name='detail_pagos'),
]