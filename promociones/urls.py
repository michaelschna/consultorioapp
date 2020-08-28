from django.contrib import admin
from django.urls import path, include
from promociones import views
urlpatterns = [
    #path('promociones/',views.medico, name="medicos"),
    path('crearpromociones/', views.crearpromociones, name="crearpromociones"),

]