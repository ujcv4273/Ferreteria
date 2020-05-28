# Generated by Django 2.2.6 on 2020-03-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0011_facturaencabezado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correoCliente',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='correoProveedor',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombreProveedor',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='turnoempleado',
            name='horaEntrada',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='turnoempleado',
            name='horaSalida',
            field=models.TimeField(),
        ),
    ]