# Generated by Django 3.0.3 on 2020-12-31 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(choices=[('PR', 'PROFESSOR'), ('HOD', 'HEAD OF DEPARTMENT'), ('AP', 'ASSOCIATE PROFESSOR'), ('AS', 'ASSISTANT PROFESSOR'), ('AF', 'ADJUNCT FACULTY'), ('TL', 'TEMPORARY LECTURER')], max_length=20)),
                ('joining_date', models.DateField(default=django.utils.timezone.localdate)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('academic_background', models.TextField(default='', max_length=500)),
                ('area_of_interest', models.TextField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('project', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('AM', 'ASSISTANT MECHANIC'), ('AP', 'ASSISTANT PROGRAMMER'), ('TO', 'TECHNICAL OFFICER'), ('LA', 'LAB ASSISTANT')], max_length=20)),
            ],
        ),
    ]
