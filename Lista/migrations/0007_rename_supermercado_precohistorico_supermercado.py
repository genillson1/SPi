# Generated by Django 4.1.7 on 2023-04-30 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lista', '0006_remove_receita_tagcategoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='precohistorico',
            old_name='Supermercado',
            new_name='supermercado',
        ),
    ]
