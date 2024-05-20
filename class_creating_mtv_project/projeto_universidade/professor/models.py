from django.db import models

class Professor(models.Model):
    RA = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    formacao = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "professores"

    def __str__(self):
        return self.nome + ' ' + str(self.RA)