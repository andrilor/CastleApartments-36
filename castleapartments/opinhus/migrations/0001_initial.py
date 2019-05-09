# Generated by Django 2.2.1 on 2019-05-09 21:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eignir', '0002_auto_20190509_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='opinhus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fra', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('til', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('eign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eignir.Eign')),
            ],
        ),
    ]
