# Generated by Django 3.2 on 2021-08-15 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de la escuela')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre del grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.CharField(max_length=50, verbose_name='Hora')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domingo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaDomingo', to='optimizacion.hora')),
                ('jueves', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaJueves', to='optimizacion.hora')),
                ('lunes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaLunes', to='optimizacion.hora')),
                ('martes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaMartes', to='optimizacion.hora')),
                ('miercoles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaMiercoles', to='optimizacion.hora')),
                ('sabado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaSabado', to='optimizacion.hora')),
                ('viernes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaViernes', to='optimizacion.hora')),
            ],
        ),
        migrations.CreateModel(
            name='Licenciatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreLicenciatura', models.CharField(max_length=200, verbose_name='Nombre de la licenciatura')),
            ],
        ),
        migrations.CreateModel(
            name='nombre_Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la materia')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optimizacion.grupo')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optimizacion.horario')),
                ('licenciatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optimizacion.licenciatura')),
                ('nombreMateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optimizacion.nombre_materia')),
            ],
        ),
        migrations.CreateModel(
            name='GrupoEstudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optimizacion.escuela')),
                ('nombreGrupoEstudio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='optimizacion.nombre_materia')),
            ],
        ),
    ]