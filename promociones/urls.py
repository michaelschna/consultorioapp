from django.contrib import admin
from django.urls import path, include
from promociones import views
urlpatterns = [
    path('listapromociones/', views.listapromociones, name="listapromociones"),
    path('crearpromociones/', views.crearpromociones, name="crearpromociones"),
    path('modificarpromociones/<int:pk>', views.modificarpromociones, name="modificarpromociones"),
    path('eliminarpromociones/<int:pk>', views.eliminarpromociones, name="eliminarpromociones"),
]