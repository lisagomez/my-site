# Generated by Django 2.2.10 on 2020-03-01 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(default='Actividad', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(default='area', help_text='Area', max_length=200, verbose_name='area')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='departamento', help_text='Departamento', max_length=200, unique=True, verbose_name='nombre')),
                ('nivel', models.CharField(default='1', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13)),
                ('curp', models.CharField(max_length=18)),
                ('nombre', models.CharField(max_length=80)),
                ('paterno', models.CharField(max_length=80)),
                ('materno', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Nombre del Puesto', help_text='Puesto', max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_rh.Area')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_rh.Departamento')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_rh.Departamento'),
        ),
    ]
