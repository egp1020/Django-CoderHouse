from django.urls import path
from .views import una_vista, crear_mascota, listar_mascotas, editar_mascota, eliminar_mascota, mostrar_mascota

urlpatterns = [
    path('', una_vista, name='index'),
    path('mascotas/', listar_mascotas, name='listar_mascotas'),
    path('crear-mascota/', crear_mascota, name='crear_mascota'),
    path('editar-mascota/<int:id>/', editar_mascota, name='editar_mascota'),
    path('eliminar-mascota/<int:id>/', eliminar_mascota, name='eliminar_mascota'),
    path('mostrar-mascota/<int:id>/', mostrar_mascota, name='mostrar_mascota'),
]