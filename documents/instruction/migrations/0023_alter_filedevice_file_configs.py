# Generated by Django 5.1.1 on 2024-11-01 03:22

import imagekit.models.fields
import instruction.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("instruction", "0022_remove_filedevice_file_report_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filedevice",
            name="file_configs",
            field=imagekit.models.fields.ProcessedImageField(
                blank=True,
                upload_to=instruction.models.path_to_file_configs,  # type: ignore
                verbose_name="Photo config",
            ),
        ),
    ]
