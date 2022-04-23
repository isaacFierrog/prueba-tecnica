from os import stat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlumnoSerializer, AlumnoDetailSerializer
from .models import Alumno


class AlumnoListAPIView(APIView):
    def get(self, request):
        alumnos = Alumno.objects.all()

        if not alumnos:
            return Response(
                {"mensaje": "No hay alumnos registrados"},
                status=status.HTTP_204_NO_CONTENT,
            )

        alumnos_serializer = AlumnoDetailSerializer(alumnos, many=True)

        return Response(
            {"mensaje": "Listado de los elementos", "data": alumnos_serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        alumno_serializer = AlumnoSerializer(data=request.data)

        if alumno_serializer.is_valid():
            alumno_serializer.save()

            return Response(
                {
                    "mensaje": "El alumno se ha agregado satisfactoriamente",
                    "data": alumno_serializer.data,
                }
            )

        return Response(
            {
                "mensaje": "No se ha podido agregar el alumno",
                "error": alumno_serializer.errors,
            }
        )


class AlumnoDetailAPIView(APIView):
    def get(self, request, id):
        alumno = Alumno.objects.filter(id=id).first()

        if not alumno:
            return Response(
                {"mensaje": "El alumno solicitado no existe"},
                status=status.HTTP_404_NOT_FOUND,
            )

        alumno_serializer = AlumnoDetailSerializer(alumno)

        return Response(
            {"mensaje": "Alumno solicitado", "data": alumno_serializer.data}
        )

    def put(self, request, id):
        alumno = Alumno.objects.filter(id=id).first()

        if not alumno:
            return Response(
                {"mensaje": "El alumno solicitado no existe"},
                status=status.HTTP_404_NOT_FOUND,
            )

        alumno_serializer = AlumnoSerializer(alumno, data=request.data)

        if alumno_serializer.is_valid():
            alumno_serializer.save()

            return Response(
                {
                    "mensaje": "El alumno se ha editado exitosamente",
                    "data": alumno_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "mensaje": "El alumno no ha podido actualizarse",
                "error": alumno_serializer.errors,
            }
        )

    def delete(self, request, id):
        alumno = Alumno.objects.filter(id=id).filter()

        if not alumno:
            return Response(
                {"mensaje": "El alumno no existe"}, status=status.HTTP_404_NOT_FOUND
            )

        alumno.delete()

        return Response(
            {
                "mensaje": "El alumno se ha borrado exitosamente",
            },
            status=status.HTTP_200_OK,
        )
