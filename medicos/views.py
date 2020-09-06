from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import MedicosForm, Medicos,UsuarioForm, Usuario

# Create your views here.
#consulta de medicos
def medico(request, plantilla="medicos.html"):
    medicos = Medicos.objects.all()
    data = {
        'medico':medicos
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearmedicos(request, plantilla="crearmedicos.html"):

    if request.method == "POST":
        form = MedicosForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('medicos')
    else:
        form = MedicosForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarmedicos(request, pk, plantilla="modificarmedicos.html"):
    if request.method == "POST":
        medico = get_object_or_404(Medicos, pk=pk)
        form = MedicosForm(request.POST or None, instance=medico)
        if form.is_valid():
            form.save()
        return redirect('medicos')
    else:
        medico = get_object_or_404(Medicos, pk=pk)
        form = MedicosForm(request.POST or None, instance=medico)



    return render(request, plantilla, {'form': form})


#pagina de eliminar
def eliminarmedicos(request, pk, plantilla="eliminarmedicos.html"):

    if request.method == "POST":
        form = MedicosForm((request.POST or None))
        medico = get_object_or_404(Medicos, pk=pk)
        if form.is_valid():
            medico.delete()
            return redirect('medicos')
    else:
        medico = get_object_or_404(Medicos, pk=pk)
        form = MedicosForm(request.POST or None, instance=medico)

    return render(request, plantilla, {'form': form})


#consulta de USUARIOS
def consultarusuario(request, plantilla="consultarusuario.html"):
    usuario = Usuario.objects.all()
    data = {
        'usuario':usuario
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearusuario(request, plantilla="crearusuario.html"):

    if request.method == "POST":
        form = UsuarioForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form = UsuarioForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarusuario(request, pk, plantilla="modificarusuario.html"):
    if request.method == "POST":
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(request.POST or None, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('usuario')
    else:
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(request.POST or None, instance=usuario)



    return render(request, plantilla, {'form': form})
#pagina de eliminar
def eliminarusuario(request, pk, plantilla="eliminarusuario.html"):

    if request.method == "POST":
        form = UsuarioForm((request.POST or None))
        usuario = get_object_or_404(Usuario, pk=pk)
        if form.is_valid():
            usuario.delete()
            return redirect('usuario')
    else:
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(request.POST or None, instance=usuario)

    return render(request, plantilla, {'form': form})