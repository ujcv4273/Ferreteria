# Generated by Django 2.2.6 on 2020-03-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0046_remove_facturadetalle_idproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturadetalle',
            name='idProducto',
            field=models.ManyToManyField(to='gestionadmin.Producto'),
        ),
    ]
