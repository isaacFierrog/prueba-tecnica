from django.contrib import admin
from .models import Nota

# Register your models here.
class NotaAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ("id", "practicas", "parciales", "examen", "promedio")


admin.site.register(Nota)
