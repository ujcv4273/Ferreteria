# Generated by Django 3.0.5 on 2020-04-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0115_auto_20200423_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Codigo_CAI',
            field=models.CharField(default='114-560-345KJ', max_length=35, verbose_name='Codigo CAI'),
        ),
    ]
