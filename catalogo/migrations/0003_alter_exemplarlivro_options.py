# Generated by Django 4.0 on 2022-02-09 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_exemplarlivro_usuario_alter_genero_nome_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exemplarlivro',
            options={'ordering': ['data_devolucao'], 'permissions': (('pode_renovar_emprestimo', 'Pode renovar empréstimo.'),)},
        ),
    ]