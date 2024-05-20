from django.shortcuts import render, get_object_or_404
from .models import Aluno

def exibe_todos_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', context={'alunos': alunos})

def exibe_aluno_especifico(request, matricula):
    aluno = get_object_or_404(Aluno, pk=matricula)
    return render(request, 'unique.html', context={'objeto': aluno})