# Generated by Django 4.1.7 on 2023-04-10 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lista', '0002_lista_supermercado_tagreceita_receita_produto_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductReceita',
            new_name='ProdutoReceita',
        ),
    ]