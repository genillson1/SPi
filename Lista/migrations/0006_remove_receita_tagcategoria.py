# Generated by Django 4.1.7 on 2023-04-17 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lista', '0005_rename_supermercado_precohistorico_supermercado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='tagCategoria',
        ),
    ]