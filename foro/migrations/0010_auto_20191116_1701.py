# Generated by Django 2.2.6 on 2019-11-16 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0009_auto_20191115_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='fecha_publicacion',
        ),
        migrations.AlterField(
            model_name='topic',
            name='anho_estreno',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)], verbose_name='Año estreno'),
        ),
    ]
