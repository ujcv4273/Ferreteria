# Generated by Django 2.2.6 on 2020-03-16 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0043_auto_20200315_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturaencabezado',
            name='idFacturaDetalle',
        ),
        migrations.AddField(
            model_name='facturadetalle',
            name='idFacturaEncabezado',
            field=models.ForeignKey(default=2344, on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.FacturaEncabezado'),
            preserve_default=False,
        ),
    ]
