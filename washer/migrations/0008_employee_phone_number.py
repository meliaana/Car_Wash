# Generated by Django 3.1.5 on 2021-01-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('washer', '0007_auto_20210124_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(default='', max_length=125, verbose_name='Phone number'),
        ),
    ]
