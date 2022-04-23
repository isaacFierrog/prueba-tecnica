from django.urls import path
from .views import DocenteListAPIView, DocenteDetailAPIView


urlpatterns = [
    path("docentes/", DocenteListAPIView.as_view(), name="lista-docentes"),
    path("docentes/<int:id>/", DocenteDetailAPIView.as_view(), name="detalles-docente"),
]
