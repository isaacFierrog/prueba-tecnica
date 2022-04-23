from rest_framework import serializers
from apps.docentes.serializers import DocenteDetailSerializer
from .models import Curso


class CursoSerializer(serializers.ModelSerializer):
    docentes = DocenteDetailSerializer(many=True)

    class Meta:
        model = Curso
        fields = "__all__"


class CursoDetailSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"

    def to_representation(self, instance):
        return {"nombre": instance.nombre}
