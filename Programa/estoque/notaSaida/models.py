from django.db import models
from produto.models import Produtos
# Create your models here.
class NotasSaidas(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    quantidade = models.IntegerField('Quantidade', default=0)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=12)

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado', auto_now=True)

    def __str__(self):
        return self.produto.produto

    class Meta:
        verbose_name = 'Saída'
        verbose_name_plural = 'Saídas'
        ordering = ['-produto']