# Generated by Django 5.1.1 on 2024-10-04 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruction', '0007_device_designation_alter_device_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaveSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rkd', models.CharField(db_index=True, max_length=15, verbose_name='Desicn to RKD')),
                ('description', models.CharField(max_length=80, verbose_name='Name equipment')),
                ('group', models.CharField(max_length=30, verbose_name='Group')),
                ('install', models.IntegerField(verbose_name='Column install')),
                ('serial_number', models.CharField(max_length=30, verbose_name='Serial number')),
                ('register', models.IntegerField(verbose_name='Register')),
                ('temp_warning', models.CharField(max_length=3, verbose_name='Temperature warning')),
                ('temp_error', models.CharField(max_length=3, verbose_name='Temperature over')),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='instruction.device', verbose_name='Binding')),
            ],
            options={
                'verbose_name': 'sensor',
                'verbose_name_plural': 'sensors',
                'db_table': 'wavesensors',
            },
        ),
    ]