from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ProductoForm, Producto
import decimal

# Create your views here.
def listapromociones(request, plantilla="listapromociones.html"):
    promociones = Producto.objects.all()
    data = {
        'promociones':promociones
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearpromociones(request, plantilla="crearpromociones.html"):

    if request.method == "POST":
        form = ProductoForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('promociones')
    else:
        form = ProductoForm
    return render(request, plantilla, {'form': form})

#pagina de crear o insertar INSERT
def modificarpromociones(request, pk, plantilla="modificarpromociones.html"):

    if request.method == "POST":
        form = ProductoForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('promociones')
    else:
        promociones = get_object_or_404(Producto, pk=pk)
        form = ProductoForm(request.POST or None, instance=promociones)

    return render(request, plantilla, {'form': form})


def eliminarpromociones(request, pk, plantilla="eliminarpromociones.html"):

    if request.method == "POST":
        form = ProductoForm((request.POST or None))
        promociones = get_object_or_404(Producto, pk=pk)
        if form.is_valid():
            promociones.delete()
            return redirect('promociones')
    else:
        promociones = get_object_or_404(Producto, pk=pk)
        form = ProductoForm(request.POST or None, instance=promociones)

    return render(request, plantilla, {'form': form})