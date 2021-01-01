# Generated by Django 3.0.3 on 2020-12-31 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=50)),
                ('sponsored', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('dates', models.CharField(max_length=50)),
                ('organizers', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('websitelink', models.CharField(max_length=100)),
                ('cfp', models.CharField(max_length=50)),
                ('paperdue', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Workshops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('dates', models.CharField(max_length=50)),
                ('organizers', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
    ]