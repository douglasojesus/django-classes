from django.urls import path, include
from .views import *

urlpatterns = [
    path('all/', exibe_todos_alunos),
    path('all/<int:matricula>', exibe_aluno_especifico)
]
