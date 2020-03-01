from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.TextField(max_length=50, null=False)
    marca = models.TextField(null=False)
    preco = models.FloatField(null=False)
    status = models.BooleanField(null=False, default=1)
    quantidade = models.IntegerField(null=False)

    def __str__(self):
        return self.nome
