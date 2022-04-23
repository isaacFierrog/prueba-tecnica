from django.db import models
from apps.docentes.models import Docente


class Curso(models.Model):
    nombre = models.CharField(
        "Nombre del curso", max_length=50, unique=True, blank=False, null=False
    )
    descripcion = models.TextField("Descripcion del curso", blank=True, null=True)
    duracion = models.PositiveIntegerField("Duracion del curso", default=3)
    docentes = models.ManyToManyField(Docente, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
