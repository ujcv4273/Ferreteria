# Generated by Django 2.2.6 on 2020-03-16 00:50

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0030_remove_planilla_antiguedad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='nombreEmpleado',
            field=models.CharField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre]),
        ),
        migrations.AlterField(
            model_name='facturadetalle',
            name='cantidad',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarquenoseacero]),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='sueldoBase',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarsueldo]),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(max_length=40, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre]),
        ),
    ]