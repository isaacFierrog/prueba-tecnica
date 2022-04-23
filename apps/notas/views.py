from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotaSerializer
from .models import Nota


class NotaListAPIView(APIView):
    def get(self, request):
        notas = Nota.objects.all()

        if not notas:
            return Response(
                {"mensaje": "No hay notas registradas"},
                status=status.HTTP_204_NO_CONTENT,
            )

        notas_serializer = NotaSerializer(notas)

        return Response(
            {"mensaje": "Lista de notas solicitadas", "data": notas_serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        nota_serializer = NotaSerializer(data=request.data)

        if nota_serializer.is_valid():
            nota_serializer.save()

            return Response(
                {
                    "mensaje": "La nota se ha guardado exitosamente",
                    "data": nota_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "mensaje": "No se ha podido guardar la nota",
                "error": nota_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
