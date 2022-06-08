from django.db import models

# Create your models here.
class NotaFiscal(models.Model):
    descriminacao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    enderecoCobranca = models.CharField(max_length=100)
    numNota = models.CharField(max_length=100)
    data= models.CharField(max_length=100)

    def __str__(self):
        return self.descriminacao