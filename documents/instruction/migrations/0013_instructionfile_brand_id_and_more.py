# Generated by Django 5.1.1 on 2024-10-16 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instruction", "0012_project_archive"),
    ]

    operations = [
        migrations.AddField(
            model_name="instructionfile",
            name="brand_id",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="instruction.brand",
                verbose_name="Device",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="instructionfile",
            name="device_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="instruction.device",
                verbose_name="Device",
            ),
        ),
    ]
