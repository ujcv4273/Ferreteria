# Generated by Django 3.0.4 on 2020-03-26 02:35

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0079_auto_20200325_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilla',
            name='Id_Planilla',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño]),
        ),
    ]
