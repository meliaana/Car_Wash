# Generated by Django 3.1.5 on 2021-01-28 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('washer', '0002_auto_20210128_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_completed',
        ),
    ]
