# Generated by Django 2.2.1 on 2019-05-16 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('starfsmenn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heimilisfang', models.CharField(max_length=255)),
                ('baejarfelag', models.CharField(max_length=255)),
                ('postnumer', models.IntegerField()),
                ('verd', models.IntegerField()),
                ('brunabotamat', models.IntegerField()),
                ('fasteignamat', models.IntegerField()),
                ('tegund', models.CharField(max_length=255)),
                ('lysing', models.CharField(blank=True, max_length=999)),
                ('staerd', models.IntegerField()),
                ('byggingarar', models.DateField()),
                ('fjoldi_herbergja', models.IntegerField()),
                ('fjoldi_badherberga', models.IntegerField()),
                ('fjoldi_svefnherberga', models.IntegerField()),
                ('sett_a_solu', models.DateField()),
                ('laust_nuna', models.BooleanField()),
                ('teikning', models.BooleanField()),
                ('serinngangur', models.BooleanField()),
                ('sameigninlegur_inngangur', models.BooleanField()),
                ('solpallur', models.BooleanField()),
                ('svalir', models.BooleanField()),
                ('gardur', models.BooleanField()),
                ('thvottahus', models.BooleanField()),
                ('hjolastolaadgengi', models.BooleanField()),
                ('lyfta', models.BooleanField()),
                ('bilskur', models.BooleanField()),
                ('bilastaedi', models.BooleanField()),
                ('nafn_seljanda', models.CharField(max_length=255)),
                ('simi_seljanda', models.IntegerField()),
                ('netfang_seljanda', models.CharField(max_length=255)),
                ('starfsmenn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='starfsmenn.Starfsmenn')),
            ],
        ),
        migrations.CreateModel(
            name='GPS_Stadsetning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heimilisfang', models.CharField(max_length=255)),
                ('lat', models.FloatField(max_length=(10, 6))),
                ('lng', models.FloatField(max_length=(10, 6))),
                ('eign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eignir.Eign')),
            ],
        ),
        migrations.CreateModel(
            name='Eignmynd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mynd', models.CharField(max_length=999)),
                ('eign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eignir.Eign')),
            ],
        ),
    ]
