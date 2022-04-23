from django.urls import path
from .views import AlumnoDetailAPIView, AlumnoListAPIView


urlpatterns = [
    path("alumnos/", AlumnoListAPIView.as_view(), name="lista-alumnos"),
    path("alumnos/<int:id>", AlumnoDetailAPIView.as_view(), name="detalles-alumnos"),
]
