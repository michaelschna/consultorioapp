from django.shortcuts import render, redirect
from .forms import MedicosForm, Medicos

# Create your views here.
def medico(request, plantilla="medico.html"):
    medicos = Medicos.objects.all()
    data = {
        'medico':medicos
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearmedicos(request, template_name="crearmedico.html"):

    if request.method == "POST":
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('medicos')
    else:
        form = MedicosForm

    return render(request, template_name, {'medicos':form})
