# Generated by Django 5.1.1 on 2024-10-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruction', '0011_remove_project_device_id_device_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='Archive'),
        ),
    ]