from django.contrib import admin
from .models import Alumno


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "fecha_nacimiento", "usuario")


admin.site.register(Alumno, AlumnoAdmin)
