# Generated by Django 3.0.4 on 2020-03-26 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0082_auto_20200325_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='existencia',
            new_name='Existencia',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='existenciaMinima',
            new_name='Existencia_Minima',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='idCategoria',
            new_name='Id_Categoria',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='idGarantia',
            new_name='Id_Garantia',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='idMarca',
            new_name='Id_Marca',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='idProducto',
            new_name='Id_Producto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombreProducto',
            new_name='Nombre_Producto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precioCompra',
            new_name='Precio_Compra',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precioVenta',
            new_name='Precio_Venta',
        ),
    ]