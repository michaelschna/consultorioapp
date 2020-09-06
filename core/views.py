from django.shortcuts import render, redirect

# Create your views here.

def index(request, plantilla="index.html"):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, plantilla)
    # En otro caso redireccionamos al login
    return redirect('login')

def promociones(request, plantilla="promociones.html"):
    return render(request, plantilla)

def servicios(request, plantilla="servicios.html"):
    return render(request, plantilla)



def doctores(request, plantilla="doctores.html"):
    return render(request, plantilla)

def acerca(request, plantilla="acerca.html"):
    return render(request, plantilla)





