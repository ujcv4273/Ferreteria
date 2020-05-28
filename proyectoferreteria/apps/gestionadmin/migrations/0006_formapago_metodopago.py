# Generated by Django 2.2.6 on 2020-03-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0005_garantia'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('idFormaPago', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('descripcionFormaPago', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('idMetodoPago', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('descripcionMetodoPago', models.CharField(max_length=100)),
            ],
        ),
    ]
