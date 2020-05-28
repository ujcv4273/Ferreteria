# Generated by Django 3.0.5 on 2020-04-13 21:22

from django.db import migrations, models
import django.db.models.deletion
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0110_auto_20200409_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='Descripcion_Categoria',
            field=models.CharField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='Id_Categoria',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Nombre_Cliente',
            field=models.CharField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Direccion_Empleado',
            field=models.TextField(max_length=100, validators=[proyectoferreteria.apps.gestionadmin.models.validardireccion], verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Id_Empleado',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Id_Planilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Planilla', verbose_name='Planilla'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Id_Turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.TurnoEmpleado', verbose_name='Turno'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Nombre_Empleado',
            field=models.CharField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Telefono_Empleado',
            field=models.CharField(max_length=8, validators=[proyectoferreteria.apps.gestionadmin.models.validarnumero], verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='formapago',
            name='Descripcion_Forma_Pago',
            field=models.TextField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='  Descripcion'),
        ),
        migrations.AlterField(
            model_name='formapago',
            name='Id_Forma_Pago',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='garantia',
            name='Descripcion_Garantia',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='garantia',
            name='Id_Garantia',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='garantia',
            name='Tiempo_Garantia_Mes',
            field=models.IntegerField(verbose_name='Garantia'),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='descripcionMetodoPago',
            field=models.TextField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='idMetodoPago',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='IHSS',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarnegativos], verbose_name='IHSS'),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='Id_Planilla',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='RAP',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarnegativos], verbose_name='RAP'),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='Sueldo_Base',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarsueldo], verbose_name='Sueldo Base'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Existencia',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarquenoseacero], verbose_name='Existencia'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Existencia_Minima',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validar_mayor_a_tres], verbose_name='Existencia Minima'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Id_Categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Id_Garantia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Garantia', verbose_name='Garantia'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Id_Marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Marca', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Id_Producto',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Nombre_Producto',
            field=models.CharField(max_length=40, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Precio_Compra',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarquenoseacero], verbose_name='Precio Compra'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Precio_Venta',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarquenoseacero], verbose_name='Precio Venta'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Correo_Proveedor',
            field=models.EmailField(blank=True, max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarcorreoexistenteProveedor], verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Direccion_Proveedor',
            field=models.TextField(max_length=100, validators=[proyectoferreteria.apps.gestionadmin.models.validardireccion], verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Id_Proveedor',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Nombre_Proveedor',
            field=models.CharField(max_length=35, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Telefono_Proveedor',
            field=models.CharField(max_length=8, validators=[proyectoferreteria.apps.gestionadmin.models.validarnumero], verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='turnoempleado',
            name='Hora_de_Entrada',
            field=models.CharField(max_length=5, validators=[proyectoferreteria.apps.gestionadmin.models.validarhora], verbose_name='Hora entrada'),
        ),
        migrations.AlterField(
            model_name='turnoempleado',
            name='Hora_de_Salida',
            field=models.CharField(max_length=5, validators=[proyectoferreteria.apps.gestionadmin.models.validarhora], verbose_name='Hora salida'),
        ),
        migrations.AlterField(
            model_name='turnoempleado',
            name='Id_Turno',
            field=models.AutoField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño], verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='turnoempleado',
            name='Turno',
            field=models.CharField(max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre], verbose_name='Turno'),
        ),
    ]