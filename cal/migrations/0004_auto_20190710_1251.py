# Generated by Django 2.0.13 on 2019-07-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20190710_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True),
        ),
    ]