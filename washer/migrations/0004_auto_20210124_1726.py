# Generated by Django 3.1.5 on 2021-01-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('washer', '0003_auto_20210124_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='washer',
        ),
        migrations.AddField(
            model_name='washer',
            name='employee',
            field=models.ManyToManyField(blank=True, related_name='washer', to='washer.Employee'),
        ),
    ]
