# Generated by Django 3.0.3 on 2021-01-10 15:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20210109_2358'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conferences',
            old_name='websitelink',
            new_name='website_link',
        ),
        migrations.RemoveField(
            model_name='conferences',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='conferences',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='conferences',
            name='event',
        ),
        migrations.RemoveField(
            model_name='conferences',
            name='paperdue',
        ),
        migrations.RemoveField(
            model_name='workshops',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='workshops',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='workshops',
            name='event',
        ),
        migrations.AddField(
            model_name='conferences',
            name='from_date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AddField(
            model_name='conferences',
            name='paper_submission_de',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AddField(
            model_name='conferences',
            name='to_date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AddField(
            model_name='workshops',
            name='from_date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AddField(
            model_name='workshops',
            name='to_date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AlterField(
            model_name='conferences',
            name='organizers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Faculty'),
        ),
        migrations.AlterField(
            model_name='conferences',
            name='status',
            field=models.CharField(choices=[('UP', 'Upcoming'), ('C', 'Completed')], max_length=50),
        ),
        migrations.AlterField(
            model_name='workshops',
            name='organizers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Faculty'),
        ),
        migrations.AlterField(
            model_name='workshops',
            name='status',
            field=models.CharField(choices=[('UP', 'Upcoming'), ('C', 'Completed')], max_length=50),
        ),
    ]
