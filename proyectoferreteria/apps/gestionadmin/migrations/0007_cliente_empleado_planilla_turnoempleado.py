# Generated by Django 2.2.6 on 2020-03-04 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0006_formapago_metodopago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=15)),
                ('correoCliente', models.CharField(max_length=30)),
                ('direccionCliente', models.CharField(max_length=100)),
                ('telefonoCliente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('idPlanilla', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('sueldoBase', models.IntegerField()),
                ('IHSS', models.IntegerField()),
                ('RAP', models.IntegerField()),
                ('antiguedad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TurnoEmpleado',
            fields=[
                ('idTurno', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('horaEntrada', models.CharField(max_length=5)),
                ('horaSalida', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombreEmpleado', models.CharField(max_length=15)),
                ('direccionEmpleado', models.CharField(max_length=60)),
                ('telefonoEmpleado', models.IntegerField()),
                ('idPlanilla', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Planilla')),
                ('idTurno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.TurnoEmpleado')),
            ],
        ),
    ]
