# Generated by Django 2.2.1 on 2019-05-10 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190510_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='eftirnafn',
            new_name='fullt_nafn',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='nafn',
            new_name='heimilisfang',
        ),
    ]