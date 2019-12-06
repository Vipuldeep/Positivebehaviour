# Generated by Django 2.2.3 on 2019-11-29 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_clientlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_Name', models.CharField(max_length=100)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('date_details', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='clientList',
        ),
    ]