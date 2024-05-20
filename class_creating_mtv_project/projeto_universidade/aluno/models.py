from django.db import models

class Aluno(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_ingresso = models.DateField()

    def __str__(self):
        return self.nome + ' ' + str(self.matricula)