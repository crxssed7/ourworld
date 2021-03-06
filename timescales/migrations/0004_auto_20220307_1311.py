# Generated by Django 3.2.7 on 2022-03-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timescales', '0003_remove_geoeon_eon_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoeon',
            name='absolute_number',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='geoera',
            name='absolute_number',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='geoperiod',
            name='absolute_number',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
