from django.contrib import admin
from .models import Curso, Materia, Docente, Estudiante, CursoDocenteEstudiannte
# Register your models here.
admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(Docente)
admin.site.register(Estudiante)
admin.site.register(CursoDocenteEstudiannte)

