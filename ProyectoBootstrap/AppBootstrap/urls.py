from django.urls import path
from .views import home, ListarLibros, CrearLibro, EditarLibro, EliminarLibro, MostrarLibro


urlpatterns = [
    path('', home, name='index'),
    path('libros/', ListarLibros.as_view(), name='listar_libros'),
    path('crear-libro/', CrearLibro.as_view(), name='crear_libro'),
    path('editar-libro/<int:pk>/', EditarLibro.as_view(), name='editar_libro'),
    path('eliminar-libro/<int:pk>/', EliminarLibro.as_view(), name='eliminar_libro'),
    path('mostrar-libro/<int:pk>/', MostrarLibro.as_view(), name='mostrar_libro'),
]