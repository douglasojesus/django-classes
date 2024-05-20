from django.db import models
from professor.models import Professor
from aluno.models import Aluno

class Disciplina(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=50)
    ementa = models.TextField()
    ch = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.nome + ' ' + str(self.codigo)
