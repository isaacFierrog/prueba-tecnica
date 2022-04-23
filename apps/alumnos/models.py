from tkinter.tix import Tree
from django.db import models
from apps.docentes.models import Docente
from apps.cursos.models import Curso
from apps.notas.models import Nota


class Alumno(models.Model):
    nombre = models.CharField(
        "Nombre del alumno", max_length=70, blank=False, null=False
    )
    apellido = models.CharField(
        "Apellido del alumno", max_length=70, blank=False, null=False
    )
    fecha_nacimiento = models.DateField(
        "Fecha de nacimiento", auto_now=False, auto_now_add=False, blank=True, null=True
    )
    usuario = models.CharField(
        "Nombre de usuario", max_length=50, unique=True, blank=False, null=False
    )
    password = models.CharField(
        "Contraseña del alumno", max_length=20, unique=True, blank=False, null=False
    )
    docentes = models.ManyToManyField(Docente, blank=True)
    cursos = models.ManyToManyField(Curso, blank=True)
    notas = models.ManyToManyField(Nota, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "alumno"
        verbose_name_plural = "alumnos"
