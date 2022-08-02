from re import template
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login, register, perfil, editar_perfil, ChangePasswordView

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', ChangePasswordView.as_view(), name='cambiar_password'),
]
