from django.contrib import admin
from django.urls import path, include
from medicos import views
urlpatterns = [
    #url de medicos
    path('medicos/', views.medico, name="medicos"),
    path('crearmedicos/', views.crearmedicos, name="crearmedicos"),
    path('modificarmedicos/<int:pk>', views.modificarmedicos, name="modificarmedicos"),
    path('eliminarmedicos/<int:pk>', views.eliminarmedicos, name="eliminarmedicos"),

    #url de usuarios
    path('usuario/', views.consultarusuario, name="usuario"),
    path('crearusuario/', views.crearusuario, name="crearusuario"),
    path('modificarusuario/<int:pk>', views.modificarusuario, name="modificarusuario"),
    path('eliminarusuario/<int:pk>', views.eliminarusuario, name="eliminarusuario"),
]