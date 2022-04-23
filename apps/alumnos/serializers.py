from apps.docentes.serializers import DocenteDetailSerializer
from apps.cursos.serializers import CursoDetailSerailizer
from apps.notas.serializers import NotaSerializer
from rest_framework import serializers
from .models import Alumno


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"


class AlumnoDetailSerializer(serializers.ModelSerializer):
    docentes = DocenteDetailSerializer(many=True)
    cursos = CursoDetailSerailizer(many=True)
    notas = NotaSerializer(many=True)

    class Meta:
        model = Alumno
        fields = "__all__"
