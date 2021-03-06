"""consultorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout


urlpatterns = [

    path('', views.index, name="index"),
    path('promociones', views.promociones, name="promociones"),
    path('servicios', views.servicios, name="servicios"),
    path('doctores', views.doctores, name="doctores"),
    path('acerca', views.acerca, name="acerca"),
    path('contacto', views.contacto, name="contacto"),
    #path('cita/',views.cita,name="cita"),
    path('medicos/', include('medicos.urls'),name="medicos"),
    path('usuarios/', include('usuarios.urls'), name="usuarios"),
    path('admin/', admin.site.urls),

]

