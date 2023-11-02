from django.urls import path
from .views import RazaList, RazaDetail, PerroList, PerroDetail

urlpatterns = [
    path('razas/', RazaList.as_view(), name='raza-list'),
    path('razas/<int:raza_id>/', RazaDetail.as_view(), name='raza-detail'),
    path('perros/', PerroList.as_view(), name='perro-list'),
    path('perros/<int:raza_id>/', PerroDetail.as_view(), name='perro-detail'),
]