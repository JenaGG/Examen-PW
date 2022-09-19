# Generated by Django 4.1.1 on 2022-09-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugadore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Edad', models.IntegerField()),
                ('Numero', models.IntegerField()),
                ('Equipo_perteneciente', models.CharField(max_length=50)),
                ('Fecha_de_ingreso_al_equipo', models.DateField()),
                ('Estatus', models.BooleanField(default=True)),
            ],
        ),
    ]