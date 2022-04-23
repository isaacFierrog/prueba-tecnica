from os import stat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CursoSerializer
from .models import Curso


class CursoAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()

        if not cursos:
            return Response(
                {
                    "mensaje": "No hay cursos registrados",
                },
                status=status.HTTP_204_NO_CONTENT,
            )

        cursos_serializer = CursoSerializer(cursos, many=True)

        return Response(
            {"mensaje": "Listado de cursos", "data": cursos_serializer.data}
        )

    def post(self, request):
        curso_serializer = CursoSerializer(data=request.data)

        if curso_serializer.is_valid():
            curso_serializer.save()

            return Response(
                {
                    "mensaje": "El curso se ha agregado satisfactoriamente",
                    "data": curso_serializer.validated_data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"mensaje": "Ha ocurrido un error", "error": curso_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class CursoDetailAPIView(APIView):
    def get(self, request, id):
        curso = Curso.objects.filter(id=id).first()

        if not curso:
            return Response(
                {"mensaje": "El curso no existe"}, status=status.HTTP_404_NOT_FOUND
            )

        curso_serializer = CursoSerializer(curso)

        return Response({"mensaje": "Curso encontrado", "data": curso_serializer.data})

    def put(self, request, id):
        curso = Curso.objects.filter(id=id).first()

        if not curso:
            return Response(
                {"mensaje": "El curso no existe"}, status=status.HTTP_404_NOT_FOUND
            )

        curso_serializer = CursoSerializer(curso, data=request.data)

        if curso_serializer.is_valid():
            curso_serializer.save()

            return Response(
                {
                    "mensaje": "El curso se ha actualizado satisfactoriamente",
                    "data": curso_serializer.validated_data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"mensaje": "Ha ocurrido un error", "error": curso_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, reques, id):
        curso = Curso.objects.filter(id=id).first()

        if not curso:
            if not curso:
                return Response(
                    {"mensaje": "El curso no existe"}, status=status.HTTP_404_NOT_FOUND
                )

        curso.delete()

        return Response({"mensaje": "El curso fue eliminado satisfactoriamente"})
