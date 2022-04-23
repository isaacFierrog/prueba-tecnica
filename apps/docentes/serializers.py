from dataclasses import fields
from rest_framework import serializers
from .models import Docente


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = "__all__"


class DocenteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "nombre": instance.nombre,
            "apellido": instance.apellido,
        }
