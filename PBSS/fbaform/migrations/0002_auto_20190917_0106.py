# Generated by Django 2.2.4 on 2019-09-16 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbaform', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Date_time',
        ),
        migrations.RemoveField(
            model_name='cuesofdistress',
            name='cues_id',
        ),
        migrations.RemoveField(
            model_name='location',
            name='Date_time_id',
        ),
        migrations.RemoveField(
            model_name='triggers',
            name='Location_id',
        ),
    ]