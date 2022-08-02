"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from AppCoder.views import saludo, saludo_particular, fecha_nacimiento, template_saludo_general, calcular_imc, elegir_nombre_aleatorio


urlpatterns = [
    path('', include('mascota.urls')),
    path('accounts/', include('accounts.urls')),
    path("app-coder/saludo", saludo),
    path("app-coder/saludo/<nombre>", saludo_particular),
    path("app-coder/fecha-nacimiento/<edad>", fecha_nacimiento),
    path("app-coder/saludo-template", template_saludo_general),
    path("app-coder/imc", calcular_imc),
    path("app-coder/nombre-aleatorio", elegir_nombre_aleatorio),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)