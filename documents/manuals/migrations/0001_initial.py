# Generated by Django 5.1.1 on 2024-10-28 09:11

import django.db.models.deletion
import imagekit.models.fields
import manuals.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Brand')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('icon', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=manuals.models.path_to_icon_brand, verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=80, verbose_name='Module')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, default=' ', verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuals.brand', verbose_name='Brand')),
            ],
            options={
                'verbose_name': 'module',
                'verbose_name_plural': 'modules',
                'db_table': 'modules',
            },
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='Name')),
                ('slug', models.SlugField(max_length=120, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, default=' ', verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manuals.module', verbose_name='Device')),
            ],
            options={
                'verbose_name': 'instruction',
                'verbose_name_plural': 'instructions',
                'db_table': 'instructions',
            },
        ),
        migrations.CreateModel(
            name='FileModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('file_instruction', models.FileField(blank=True, upload_to=manuals.models.path_to_file_instruction, verbose_name='Инструкция')),
                ('file_manual', models.FileField(blank=True, upload_to=manuals.models.path_to_file_manual, verbose_name='Руководство')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices_files', to='manuals.module', verbose_name='Device')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
                'db_table': 'file_modules',
            },
        ),
    ]
