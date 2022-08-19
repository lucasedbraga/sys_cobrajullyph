from django.db import models
import datetime

class Animal(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Producao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    registro = models.FloatField(max_length=3)
    horario = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.animal.nome