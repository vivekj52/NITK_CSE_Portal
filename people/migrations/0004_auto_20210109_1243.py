# Generated by Django 3.0.3 on 2021-01-09 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20210109_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='email',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='name',
        ),
        migrations.RemoveField(
            model_name='projectstaff',
            name='email',
        ),
        migrations.RemoveField(
            model_name='projectstaff',
            name='name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='name',
        ),
    ]
