from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.alumnos.urls")),
    path("api/", include("apps.cursos.urls")),
    path("api/", include("apps.docentes.urls")),
    path("api/", include("apps.notas.urls")),
]
