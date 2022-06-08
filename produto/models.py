from operator import mod
from pyexpat import model
import re
from django.db import models

# Create your models here.
class Produto(models.Model):
    cod = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    descricao= models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    valor= models.CharField(max_length=100)
    validade= models.CharField(max_length=100)

    def __str__(self):
        return self.cod