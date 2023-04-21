from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Supermercado(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nome} - {self.id}'
    

class PrecoHistorico(models.Model):
    preco = models.FloatField()
    timestamp = models.DateTimeField()
    promoTag = models.BooleanField()
    supermercado = models.ForeignKey(Supermercado, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto.nome + " - " + self.supermercado.nome + " - " + str(self.preco)
    

class Lista(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nome} - {self.id}'
    


class Lista_produto(models.Model):
    produto = models.ForeignKey(Produto,related_name='produto', on_delete=models.SET_NULL, null=True)
    lista = models.ForeignKey(Lista, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField()
    produto_second_option = models.ForeignKey(Produto, related_name='secondOption', on_delete=models.SET_NULL, null=True)
    importancia = models.IntegerField()

    def __str__(self):
        return f'{self.produto.nome} - {self.id}'
    

class TagReceita(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Receita(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.nome} - {self.id}'
    

class ProdutoReceita(models.Model):
    produto = models.ForeignKey(Produto,related_name='prod_in_receita', on_delete=models.SET_NULL, null=True)
    receita = models.ForeignKey(Receita, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.id}  - {self.produto}  - {self.receita}'
