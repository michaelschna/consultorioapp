from django.contrib import admin
from django.urls import path, include
from medicos import views
urlpatterns = [
    path('medicos/',views.medico, name="medicos"),
    path('crearmedicos/', views.crearmedicos, name="crearmedicos"),
]