from django.db import models

# Create your models here.
class Padarias(models.Model):
    nome: models.CharField('Nome', max_length=100)
    endereco: models.CharField('Endereço', max_length=100)
    telefone: models.CharField('Telefone', max_length=12)
