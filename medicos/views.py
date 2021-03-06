from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import *
from .models import *
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

#paciente
def consultarpaciente(request, plantilla="consultarpaciente.html"):
    paciente = Paciente.objects.all()
    data = {
        'paciente':paciente
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearpaciente(request, plantilla="crearpaciente.html"):

    if request.method == "POST":
        form = PacienteForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('paciente')
    else:
        form = PacienteForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarpaciente(request, pk, plantilla="modificarpaciente.html"):
    if request.method == "POST":
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(request.POST or None, instance=paciente)
        if form.is_valid():
            form.save()
        return redirect('paciente')
    else:
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(request.POST or None, instance=paciente)



    return render(request, plantilla, {'form': form})
#pagina de eliminar
def eliminarpaciente(request, pk, plantilla="eliminarpaciente.html"):

    if request.method == "POST":
        form = PacienteForm((request.POST or None))
        paciente = get_object_or_404(Paciente, pk=pk)
        if form.is_valid():
            paciente.delete()
            return redirect('paciente')
    else:
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(request.POST or None, instance=paciente)

    return render(request, plantilla, {'form': form})


#dia de atencion
def consultardiadeatencion(request, plantilla="consultardiadeatencion.html"):
    dia_atencion = Dia_atencion.objects.all()
    data = {
        'diadeatencion':dia_atencion
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def creardiadeatencion(request, plantilla="creardiadeatencion.html"):

    if request.method == "POST":
        form = Dia_atencionForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('diadeatencion')
    else:
        form = Dia_atencionForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificardiadeatencion(request, pk, plantilla="modificardiadeatencion.html"):
    if request.method == "POST":
        dia_atencion = get_object_or_404(Dia_atencion, pk=pk)
        form = Dia_atencionForm(request.POST or None, instance=dia_atencion)
        if form.is_valid():
            form.save()
        return redirect('diadeatencion')
    else:
        dia_atencion = get_object_or_404(Dia_atencion, pk=pk)
        form = Dia_atencionForm(request.POST or None, instance=dia_atencion)



    return render(request, plantilla, {'form': form})
#pagina de eliminar
def eliminardiadeatencion(request, pk, plantilla="eliminardiadeatencion.html"):

    if request.method == "POST":
        form = Dia_atencionForm((request.POST or None))
        dia_atencion = get_object_or_404(Dia_atencion, pk=pk)
        if form.is_valid():
            dia_atencion.delete()
            return redirect('diadeatencion')
    else:
        dia_atencion = get_object_or_404(Dia_atencion, pk=pk)
        form = Dia_atencionForm(request.POST or None, instance=dia_atencion)

    return render(request, plantilla, {'form': form})


#horario de atenciones
def consultarhorariodeatencion(request, plantilla="consultarhorariodeatencion.html"):
    horario_atencion = Horario_atencion.objects.all()
    data = {
        'horariodeatencion':horario_atencion
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearhorariodeatencion(request, plantilla="crearhorariodeatencion.html"):

    if request.method == "POST":
        form = Horario_atencionForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('horariodeatencion')
    else:
        form = Horario_atencionForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarhorariodeatencion(request, pk, plantilla="modificarhorariodeatencion.html"):
    if request.method == "POST":
        horario_atencion = get_object_or_404(Horario_atencion, pk=pk)
        form = Horario_atencionForm(request.POST or None, instance=horario_atencion)
        if form.is_valid():
            form.save()
        return redirect('horariodeatencion')
    else:
        horario_atencion = get_object_or_404(Horario_atencion, pk=pk)
        form = Horario_atencionForm(request.POST or None, instance=horario_atencion)



    return render(request, plantilla, {'form': form})
#pagina de eliminar
def eliminarhorariodeatencion(request, pk, plantilla="eliminarhorariodeatencion.html"):

    if request.method == "POST":
        form = Horario_atencionForm((request.POST or None))
        horario_atencion = get_object_or_404(Horario_atencion, pk=pk)
        if form.is_valid():
            horario_atencion.delete()
            return redirect('horariodeatencion')
    else:
        horario_atencion = get_object_or_404(Horario_atencion, pk=pk)
        form = Horario_atencionForm(request.POST or None, instance=horario_atencion)

    return render(request, plantilla, {'form': form})


#antecedentes
def consultarantecedentes(request, plantilla="consultarantecedentes.html"):
    antecedente = Antecedente.objects.all()
    data = {
        'antecedente':antecedente
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearantecedentes(request, plantilla="crearantecedentes.html"):

    if request.method == "POST":
        form = AntecedenteForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('antecedentes')
    else:
        form = AntecedenteForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarantecedentes(request, pk, plantilla="modificarantecedentes.html"):
    if request.method == "POST":
        antecedente = get_object_or_404(Antecedente, pk=pk)
        form = AntecedenteForm(request.POST or None, instance=antecedente)
        if form.is_valid():
            form.save()
        return redirect('antecedentes')
    else:
        antecedente = get_object_or_404(Antecedente, pk=pk)
        form = AntecedenteForm(request.POST or None, instance=antecedente)



    return render(request, plantilla, {'form': form})
#pagina de eliminar
def eliminarantecedentes(request, pk, plantilla="eliminarantecedentes.html"):

    if request.method == "POST":
        form = AntecedenteForm((request.POST or None))
        antecedente = get_object_or_404(Antecedente, pk=pk)
        if form.is_valid():
            antecedente.delete()
            return redirect('antecedentes')
    else:
        antecedente = get_object_or_404(Antecedente, pk=pk)
        form = AntecedenteForm(request.POST or None, instance=antecedente)

    return render(request, plantilla, {'form': form})

#examenes
def consultarexamen(request, plantilla="consultarexamen.html"):
    examen = Examen.objects.all()
    data = {
        'examen':examen
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearexamen(request, plantilla="crearexamen.html"):

    if request.method == "POST":
        form = ExamenForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('examen')
    else:
        form = ExamenForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarexamen(request, pk, plantilla="modificarexamen.html"):
    if request.method == "POST":
        examen = get_object_or_404(Examen, pk=pk)
        form = ExamenForm(request.POST or None, instance=examen)
        if form.is_valid():
            form.save()
        return redirect('examen')
    else:
        examen = get_object_or_404(Examen, pk=pk)
        form = ExamenForm(request.POST or None, instance=examen)



    return render(request, plantilla, {'form': form})
#pagina de eliminar
def eliminarexamen(request, pk, plantilla="eliminarexamen.html"):

    if request.method == "POST":
        form = ExamenForm((request.POST or None))
        examen = get_object_or_404(Examen, pk=pk)
        if form.is_valid():
            examen.delete()
            return redirect('examen')
    else:
        examen = get_object_or_404(Examen, pk=pk)
        form = ExamenForm(request.POST or None, instance=examen)

    return render(request, plantilla, {'form': form})


#consulta
def consultarconsulta(request, plantilla="consultarconsulta.html"):
    consulta = Consulta.objects.all()
    data = {
        'consulta':consulta
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearconsulta(request, plantilla="crearconsulta.html"):

    if request.method == "POST":
        form = ConsultaForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('consulta')
    else:
        form = ConsultaForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarconsulta(request, pk, plantilla="modificarconsulta.html"):
    if request.method == "POST":
        consulta = get_object_or_404(Consulta, pk=pk)
        form = ConsultaForm(request.POST or None, instance=consulta)
        if form.is_valid():
            form.save()
        return redirect('consulta')
    else:
        consulta = get_object_or_404(Consulta, pk=pk)
        form = ConsultaForm(request.POST or None, instance=consulta)



    return render(request, plantilla, {'form': form})
#pagina de eliminar
def eliminarconsulta(request, pk, plantilla="eliminarconsulta.html"):

    if request.method == "POST":
        form = ConsultaForm((request.POST or None))
        consulta = get_object_or_404(Consulta, pk=pk)
        if form.is_valid():
            consulta.delete()
            return redirect('consulta')
    else:
        consulta = get_object_or_404(Consulta, pk=pk)
        form = ConsultaForm(request.POST or None, instance=consulta)

    return render(request, plantilla, {'form': form})


#examen de consulta
def consultarexamenconsulta(request, plantilla="consultarexamenconsulta.html"):
    examenconsulta = Examen_consulta.objects.all()
    data = {
        'examenconsulta':examenconsulta
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearexamenconsulta(request, plantilla="crearexamenconsulta.html"):

    if request.method == "POST":
        form = Examen_consultaForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('examenconsulta')
    else:
        form = Examen_consultaForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarexamenconsulta(request, pk, plantilla="modificarexamenconsulta.html"):
    if request.method == "POST":
        examenconsulta = get_object_or_404(Examen_consulta, pk=pk)
        form = Examen_consultaForm(request.POST or None, instance=examenconsulta)
        if form.is_valid():
            form.save()
        return redirect('examenconsulta')
    else:
        examenconsulta = get_object_or_404(Examen_consulta, pk=pk)
        form = Examen_consultaForm(request.POST or None, instance=examenconsulta)



    return render(request, plantilla, {'form': form})
#pagina de eliminar
def eliminarexamenconsulta(request, pk, plantilla="eliminarexamenconsulta.html"):

    if request.method == "POST":
        form = Examen_consultaForm((request.POST or None))
        examenconsulta = get_object_or_404(Examen_consulta, pk=pk)
        if form.is_valid():
            examenconsulta.delete()
            return redirect('examenconsulta')
    else:
        examenconsulta = get_object_or_404(Examen_consulta, pk=pk)
        form = Examen_consultaForm(request.POST or None, instance=examenconsulta)

    return render(request, plantilla, {'form': form})