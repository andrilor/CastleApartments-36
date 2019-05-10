# Generated by Django 2.2.1 on 2019-05-10 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Starfsmadurmynd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mynd', models.CharField(max_length=999)),
            ],
        ),
        migrations.CreateModel(
            name='Starfsmenn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nafn', models.CharField(max_length=255)),
                ('simi', models.IntegerField()),
                ('netfang', models.CharField(max_length=255)),
                ('starfsheiti', models.CharField(max_length=255)),
                ('lysing', models.CharField(blank=True, max_length=999)),
                ('starfsmadurmynd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starfsmenn.Starfsmadurmynd')),
            ],
        ),
    ]
