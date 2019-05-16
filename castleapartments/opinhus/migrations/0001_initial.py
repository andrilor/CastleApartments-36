# Generated by Django 2.2.1 on 2019-05-16 17:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eignir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='opinhus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fra', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('til', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('eign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='er_opid', to='eignir.Eign')),
            ],
        ),
    ]
