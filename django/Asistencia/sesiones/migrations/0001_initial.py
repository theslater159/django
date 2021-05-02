# Generated by Django 3.2 on 2021-04-30 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Espacio_academico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('espacio', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('celular', models.CharField(max_length=25)),
                ('cedula', models.IntegerField(unique=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('semestre', models.IntegerField()),
            ],
            options={
                'verbose_name': 'estudiante',
                'verbose_name_plural': 'estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id_semestre', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sesiones',
            fields=[
                ('id_sesion', models.AutoField(primary_key=True, serialize=False)),
                ('sesion', models.CharField(max_length=25)),
                ('fecha', models.DateTimeField()),
                ('horainicio', models.TimeField()),
                ('horafin', models.TimeField()),
                ('id_espacio_academico', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sesiones.espacio_academico')),
                ('id_estudiante', models.ManyToManyField(blank=True, through='sesiones.Asistencia', to='sesiones.Estudiantes')),
            ],
            options={
                'verbose_name': 'sesion',
                'verbose_name_plural': 'sesiones',
            },
        ),
        migrations.AddField(
            model_name='espacio_academico',
            name='id_estudiante',
            field=models.ManyToManyField(blank=True, to='sesiones.Estudiantes'),
        ),
        migrations.AddField(
            model_name='espacio_academico',
            name='id_semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesiones.semestre'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='id_estudiante',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sesiones.estudiantes'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='id_sesion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesiones.sesiones'),
        ),
    ]
