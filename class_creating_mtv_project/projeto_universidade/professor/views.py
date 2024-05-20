from django.shortcuts import render, get_object_or_404
from .models import Professor

# Create your views here.
def exibe_todos_profs(request):
    professores = Professor.objects.all()
    return render(request, 'indexprof.html', context={'professores': professores})

def exibe_prof_especifico(request, ra):
    professor = get_object_or_404(Professor, pk=ra)
    return render(request, 'uniqueprof.html', context={'objeto': professor})