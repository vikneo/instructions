# Generated by Django 5.1.1 on 2024-10-04 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruction', '0005_remove_file_description_file_file_configs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
    ]
