# Generated by Django 4.0.5 on 2022-07-22 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clapperboardApp', '0007_alter_pelicula_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-creado']},
        ),
    ]