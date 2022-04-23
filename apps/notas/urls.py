from django.urls import path
from .views import NotaListAPIView


urlpatterns = [path("notas/", NotaListAPIView.as_view(), name="lista-notas")]
