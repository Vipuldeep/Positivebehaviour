# Generated by Django 2.2.3 on 2020-01-07 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20200107_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='gender',
        ),
    ]
