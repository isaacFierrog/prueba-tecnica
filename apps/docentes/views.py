from msilib.schema import ReserveCost
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocenteSerializer
from .models import Docente


class DocenteListAPIView(APIView):
    def get(self, request):
        docentes = Docente.objects.all()

        if not docentes:
            return Response(
                {"mensaje": "No hay docentes registrados"},
                status=status.HTTP_204_NO_CONTENT,
            )

        docentes_serializer = DocenteSerializer(docentes, many=True)

        return Response(
            {
                "mensaje": "Lista de docentes solicitada",
                "data": docentes_serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        docente_serializer = DocenteSerializer(data=request.data)

        if docente_serializer.is_valid():
            docente_serializer.save()

            return Response(
                {
                    "mensaje": "El docente se ha agregado exitosamente",
                    "data": docente_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "mensaje": "El docente no pudo agregarse",
                "data": docente_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class DocenteDetailAPIView(APIView):
    def get(self, request, id):
        docente = Docente.objects.filter(id=id).first()

        if not docente:
            return Response(
                {"mensaje": "El docente no existe"}, status=status.HTTP_404_NOT_FOUND
            )

        docente_serializer = DocenteSerializer(docente)

        return Response(
            {"mensaje": "Docente solicitado", "data": docente_serializer.data},
            status=status.HTTP_200_OK,
        )

    def put(self, request, id):
        docente = Docente.objects.filter(id=id).first()

        if not docente:
            return Response(
                {"mensaje": "El docente no existe"}, status=status.HTTP_404_NOT_FOUND
            )

        docente_serializer = DocenteSerializer(docente, data=request.data)

        if docente_serializer.is_valid():
            docente_serializer.save()

            return Response(
                {
                    "mensaje": "El docente se ha actualizado exitosamente",
                    "data": docente_serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "mensaje": "El docente no ha podido actualizarse",
                "error": docente_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, id):
        docente = Docente.objects.filter(id=id).first()

        if not docente:
            return Response(
                {"mensaje": "El docente no existe"}, status=status.HTTP_404_NOT_FOUND
            )

        docente.delete()

        return Response(
            {"mensaje": "El docente se ha actualizado exitosamente"},
            status=status.HTTP_200_OK,
        )
