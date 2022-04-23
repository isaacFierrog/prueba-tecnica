from django.db import models


class Docente(models.Model):
    nombre = models.CharField(
        "Nombre del docente", max_length=70, blank=False, null=False
    )
    apellido = models.CharField(
        "Apellido del docente", max_length=70, blank=False, null=False
    )
    fecha_nacimiento = models.DateField(
        "Fecha de nacimiento", auto_now=False, auto_now_add=False, blank=True, null=True
    )
    usuario = models.CharField(
        "Nombre de usuario", max_length=50, unique=True, blank=False, null=False
    )
    password = models.CharField(
        "Contraseña del docente", max_length=20, unique=True, blank=False, null=False
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "docente"
        verbose_name_plural = "docentes"
