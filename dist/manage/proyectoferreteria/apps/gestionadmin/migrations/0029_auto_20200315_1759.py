# Generated by Django 2.2.6 on 2020-03-15 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0028_auto_20200315_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnoempleado',
            name='idTurno',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
