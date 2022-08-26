from django.db import models

class Marca(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

...

class Cor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Cores"


class Carro(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="carro", default=""
    )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="carro", default= ""
    )
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="carro", default= ""
    )


    def __str__(self):
        return f'{self.nome} ({self.quantidade})'