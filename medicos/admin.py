from django.contrib import admin
from .models import Medicos, Usuario, Paciente, Dia_atencion, Horario_atencion, Antecedente, Examen
from .models import Consulta,Examen_consulta, Antecedente_consulta,Horario_medico, Tratamiento, Reservaciones
# Register your models here.
admin.site.register(Medicos)
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Dia_atencion)
admin.site.register(Horario_atencion)
admin.site.register(Antecedente)
admin.site.register(Examen)
admin.site.register(Consulta)
admin.site.register(Examen_consulta)
admin.site.register(Antecedente_consulta)
admin.site.register(Horario_medico)
admin.site.register(Tratamiento)
admin.site.register(Reservaciones)


