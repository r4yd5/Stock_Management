# Generated by Django 4.0.6 on 2022-08-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sitio_link',
            field=models.CharField(blank=True, max_length=155),
        ),
    ]
