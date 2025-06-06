# Generated by Django 5.1.1 on 2024-10-04 03:28
from typing import List

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Brand"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=100, unique=True, verbose_name="URL"),
                ),
            ],
            options={
                "verbose_name": "brand",
                "verbose_name_plural": "brands",
                "db_table": "brands",
            },
        ),
        migrations.CreateModel(
            name="Network",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=120, verbose_name="Name"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=120, unique=True, verbose_name="URL"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default=" ", verbose_name="Description"
                    ),
                ),
            ],
            options={
                "verbose_name": "network",
                "verbose_name_plural": "networks",
                "db_table": "networks",
            },
        ),
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=150, verbose_name="Device"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=150, unique=True, verbose_name="URL"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default=" ", verbose_name="Description"
                    ),
                ),
                (
                    "brand_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="brands",
                        to="instruction.brand",
                        verbose_name="Device",
                    ),
                ),
                (
                    "device_id",
                    models.ManyToManyField(
                        to="instruction.network", verbose_name="Netork"
                    ),
                ),
            ],
            options={
                "verbose_name": "device",
                "verbose_name_plural": "devices",
                "db_table": "devices",
            },
        ),
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=120, verbose_name="Name"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default=" ", verbose_name="Description"
                    ),
                ),
                (
                    "device_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="devices_files",
                        to="instruction.device",
                        verbose_name="Photo",
                    ),
                ),
            ],
            options={
                "verbose_name": "photo",
                "verbose_name_plural": "photos",
                "db_table": "files",
            },
        ),
        migrations.CreateModel(
            name="InstructionFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=120, verbose_name="Name"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=120, unique=True, verbose_name="URL"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default=" ", verbose_name="Description"
                    ),
                ),
                (
                    "device_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="devices_instructs",
                        to="instruction.device",
                        verbose_name="Instruction",
                    ),
                ),
            ],
            options={
                "verbose_name": "instruction",
                "verbose_name_plural": "instructions",
                "db_table": "instructions",
            },
        ),
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(unique=True, verbose_name="URL")),
                (
                    "slave_id",
                    models.IntegerField(blank=True, null=True, verbose_name="Slave ID"),
                ),
                (
                    "speed",
                    models.IntegerField(
                        choices=[
                            (0, "Not Used"),
                            (1200, "1200"),
                            (2400, "2400"),
                            (4800, "4800"),
                            (9600, "9600"),
                            (19200, "19200"),
                            (38400, "38400"),
                            (57600, "57600"),
                            (115200, "115200"),
                        ],
                        default=0,
                        verbose_name="Speed",
                    ),
                ),
                (
                    "paritet",
                    models.CharField(
                        choices=[
                            ("-", "Not Used"),
                            ("E", "Even"),
                            ("N", "None"),
                            ("O", "Odd"),
                        ],
                        default="-",
                        max_length=1,
                        verbose_name="Paritet",
                    ),
                ),
                (
                    "bit",
                    models.IntegerField(
                        choices=[(0, "Not Used"), (7, "7"), (8, "8"), (9, "9")],
                        default=0,
                        verbose_name="Bits",
                    ),
                ),
                (
                    "stop_bit",
                    models.IntegerField(
                        choices=[(0, "Not Used"), (1, "1"), (2, "2")],
                        default=0,
                        verbose_name="Stop bit",
                    ),
                ),
                (
                    "ip_address",
                    models.CharField(
                        default="not used", max_length=15, verbose_name="IP address"
                    ),
                ),
                (
                    "mask",
                    models.CharField(
                        default="not used", max_length=15, verbose_name="Mask"
                    ),
                ),
                (
                    "gateway",
                    models.CharField(
                        default="not used", max_length=15, verbose_name="Gateway"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default=" ", verbose_name="Description"
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="devices_settings",
                        to="instruction.device",
                        verbose_name="Device",
                    ),
                ),
                (
                    "interface",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="instruction.network",
                        verbose_name="Interface",
                    ),
                ),
            ],
            options={
                "verbose_name": "setting",
                "verbose_name_plural": "settings",
                "db_table": "settings",
            },
        ),
    ]
