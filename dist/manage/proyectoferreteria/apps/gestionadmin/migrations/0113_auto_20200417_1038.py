# Generated by Django 3.0.4 on 2020-04-17 10:38

from django.db import migrations, models
import django.db.models.deletion
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0112_auto_20200417_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='ISV15',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarnegativos], verbose_name='ISV al 15%'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='ISV18',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarnegativos], verbose_name='ISV al 18%'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Id_Cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Id_Empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Empleado', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Id_FormaPago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.FormaPago', verbose_name='Forma de oago'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Id_MetodoPago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.MetodoPago', verbose_name='Metodo de pago'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Id_producto',
            field=models.ManyToManyField(to='gestionadmin.Producto', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Numero_Sar',
            field=models.CharField(default='004-340-345KN', max_length=15, verbose_name='Numero de la SAR'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='Total_Factura',
            field=models.IntegerField(verbose_name='Total'),
        ),
    ]
