# Generated by Django 2.2.6 on 2020-04-09 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0104_auto_20200409_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Id_Cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Cliente'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Id_Empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Empleado'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Id_FormaPago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.FormaPago'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Id_MetodoPago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.MetodoPago'),
        ),
    ]
