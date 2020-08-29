from django.shortcuts import render, redirect
from .forms import ProductoForm

# Create your views here.
def crearpromociones(request, template_name="crearpromociones.html"):

    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('promociones')
    else:
        form = ProductoForm

    return render(request, template_name, {'promociones':form})