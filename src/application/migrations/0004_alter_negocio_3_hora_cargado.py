# Generated by Django 4.1 on 2022-08-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_negocio_1_hora_cargado_negocio_2_hora_cargado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negocio_3',
            name='hora_cargado',
            field=models.CharField(max_length=20),
        ),
    ]
