# Generated by Django 2.2.6 on 2020-03-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0012_auto_20200313_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='existenciaMinima',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
