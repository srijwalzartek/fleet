# Generated by Django 2.1.15 on 2020-12-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201201_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclemaster',
            name='veh',
        ),
        migrations.AlterField(
            model_name='vehiclemaster',
            name='vehmas_code',
            field=models.CharField(default='Test', max_length=50, verbose_name='Vehicle Number'),
            preserve_default=False,
        ),
    ]
