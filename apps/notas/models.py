from django.db import models
from apps.cursos.models import Curso


class Nota(models.Model):
    practicas = models.FloatField("Calificaciones practicas", blank=False, null=False)
    parciales = models.FloatField("Calificaciones practicas", blank=False, null=False)
    examen = models.FloatField("Calificaciones practicas", blank=False, null=False)
    promedio = models.FloatField("Promedio final", blank=False, null=False)
    cursos = models.ManyToManyField(Curso, blank=True)

    def __str__(self):
        return str(self.promedio)

    class Meta:
        verbose_name = "nota"
        verbose_name_plural = "nota"
