# Generated by Django 2.2.4 on 2020-02-03 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_fba', '0005_remove_fba_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fba',
            name='client_fk',
        ),
        migrations.AlterField(
            model_name='fba',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Post'),
        ),
    ]