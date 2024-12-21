
from django.urls import path
from Releyendo import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('libros/', views.libros, name="libros"),
    path('sobremi/', views.sobremi, name="sobremi"),
    path('cuenta/', views.cuenta, name="cuenta"),
    path('salir/', views.salir, name="salir"),

]