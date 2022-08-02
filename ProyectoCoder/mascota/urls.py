from django.urls import path

from accounts.views import home
from .views import ListarMascotas, CrearMascota, EditarMascota, EliminarMascota, MostrarMascota


urlpatterns = [
    path('', home, name='index'),
    path('mascotas/', ListarMascotas.as_view(), name='listar_mascotas'),
    path('crear-mascota/', CrearMascota.as_view(), name='crear_mascota'),
    path('editar-mascota/<int:pk>/', EditarMascota.as_view(), name='editar_mascota'),
    path('eliminar-mascota/<int:pk>/', EliminarMascota.as_view(), name='eliminar_mascota'),
    path('mostrar-mascota/<int:pk>/', MostrarMascota.as_view(), name='mostrar_mascota'),
]