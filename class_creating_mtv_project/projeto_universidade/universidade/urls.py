from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/', include('aluno.urls')),
    path('professor/', include('professor.urls')),
    path('disciplina/', include('disciplina.urls')),
]
