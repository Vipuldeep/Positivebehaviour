# Generated by Django 2.2.4 on 2020-02-03 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_fba', '0008_auto_20200203_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='br',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Post'),
        ),
    ]