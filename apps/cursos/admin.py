from django.contrib import admin
from .models import Curso


class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion", "duracion")
    ordering = ["nombre"]


admin.site.register(Curso, CursoAdmin)
