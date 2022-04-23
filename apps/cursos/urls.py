from django.urls import path
from .views import CursoAPIView, CursoDetailAPIView


urlpatterns = [
    path("cursos/", CursoAPIView.as_view(), name="listar-cursos"),
    path("cursos/<int:id>/", CursoDetailAPIView.as_view(), name="detalles-curso"),
]
