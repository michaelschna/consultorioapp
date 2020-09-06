from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "tr_curso"
        verbose_name = "curso"
        verbose_name_plural = "cursos"

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    nombre = models.CharField(max_length=50)

    # cursos = models.ManyToManyField(Curso)

    class Meta:
        db_table = "tr_materia"
        verbose_name = "materia"
        verbose_name_plural = "materias"

    def __str__(self):
        return self.nombre


# Create your models here.
class Docente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField(default=10)
    email = models.EmailField(default="ii@itsgg.edu.ec")
    sexo = models.CharField(max_length=1)
    estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_docente"
        verbose_name = "docente"
        verbose_name_plural = "docentes"

    def __str__(self):
        return self.apellido + ' ' + self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField(default=10)
    sexo = models.CharField(max_length=1)
    estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_estudiante"
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

    def __str__(self):
        return self.apellido


class CursoDocenteEstudiannte(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    class Meta:
        db_table = "tr_cursodocenteestudiante"


