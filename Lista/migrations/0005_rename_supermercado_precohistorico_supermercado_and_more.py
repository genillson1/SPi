# Generated by Django 4.1.7 on 2023-04-17 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lista', '0004_alter_lista_produto_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='precohistorico',
            old_name='supermercado',
            new_name='Supermercado',
        ),
        migrations.AlterField(
            model_name='receita',
            name='tagCategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Lista.categoria'),
        ),
    ]
