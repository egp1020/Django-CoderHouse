from django.urls import path
from . import views

urlpatterns = [
    path('gatos/', views.ListadoGatos.as_view(), name='listado_gatos'),
    path('crear-gato/', views.CrearGato.as_view(), name='crear_gato'),
    path('editar-gato/<int:pk>/', views.EditarGato.as_view(), name='editar_gato'),
    path('eliminar-gato/<int:pk>/', views.EliminarGato.as_view(), name='eliminar_gato'),
    path('mostrar-gato/<int:pk>/', views.MostrarGato.as_view(), name='mostrar_gato'),
]