# Generated by Django 2.2.6 on 2020-03-15 22:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0020_auto_20200315_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurnoEmpleado',
            fields=[
                ('idTurno', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('horaEntrada', models.TimeField(default=datetime.time(0, 0))),
                ('horaSalida', models.TimeField(default=datetime.time(0, 0))),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='idTurno',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.TurnoEmpleado'),
            preserve_default=False,
        ),
    ]
