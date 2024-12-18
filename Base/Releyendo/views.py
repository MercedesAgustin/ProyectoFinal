from django.shortcuts import render
from django.http import HttpResponse

def inicio(request) :
    return render ( request, "Releyendo/inicio.html")

def libros(request) :
    return render ( request, "Releyendo/libros.html")

def sobremi(request) :
    return render ( request, "Releyendo/sobremi.html")