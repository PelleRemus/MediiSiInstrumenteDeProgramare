# Generated by Django 2.2.6 on 2019-11-14 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherStation', '0002_auto_20191114_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='locationId',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='weatherTypeId',
            new_name='weatherType',
        ),
    ]
