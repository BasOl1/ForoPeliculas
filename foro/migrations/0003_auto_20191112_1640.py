# Generated by Django 2.2.6 on 2019-11-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0002_comentario_genero_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
