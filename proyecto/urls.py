"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from fitness.views import UsuarioList, UsuarioDetail, UsuarioClear, UsuarioUpdate, UsuarioCreate, register, pesos, ejercicio,calorias

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    path('admin/', admin.site.urls),
 
    path('usuarios/', UsuarioList.as_view(template_name = "fitness/usuarios.html"), name='usuarios'),
 
    path('usuarios/detalle/<int:pk>', UsuarioDetail.as_view(template_name = "fitness/detalles.html"), name='detalles'),
 
    path('usuarios/crear', UsuarioCreate.as_view(template_name = "fitness/crear.html"), name='crear'),

    path('usuarios/editar/<int:pk>', UsuarioUpdate.as_view(template_name = "fitness/actualizar.html"), name='actualizar'), 
 
    path('usuarios/eliminar/<int:pk>', UsuarioClear.as_view(), name='eliminar'),

    path('registrar/', register),

    path('ejercicio/', ejercicio ),

    path('pesos/', pesos ),

    path('calorias/', calorias),
]
