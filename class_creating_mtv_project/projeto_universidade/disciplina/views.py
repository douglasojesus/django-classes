from django.shortcuts import render, get_object_or_404
from .models import Disciplina

# Create your views here.
def exibe_todos_disc(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'indexdisc.html', context={'disciplinas': disciplinas})

def exibe_disc_especifico(request, codigo):
    disciplina = get_object_or_404(Disciplina, pk=codigo)
    return render(request, 'uniquedisc.html', context={'objeto': disciplina})