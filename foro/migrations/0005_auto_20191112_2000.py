# Generated by Django 2.2.6 on 2019-11-12 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0004_usuario_confirmar_pw'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='foro\\static\\images\\portadas'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='descargar',
            field=models.TextField(blank=True, null=True),
        ),
    ]
