# Generated by Django 2.2.3 on 2020-01-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_post_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2),
        ),
    ]
