from django.db import models


class Fotografia(models.Model):
    nome = models.CharField('Nome', max_length=100, null=False, blank=False)
    legenda = models.CharField('Legenda', max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome