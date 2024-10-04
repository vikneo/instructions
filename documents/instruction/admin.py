from django.contrib import admin
from .models import (
    Brand, 
    Device,
    InstructionFile,
    File,
    Network,
    Settings,
    Project
    )


class FileTabularInline(admin.TabularInline):
    model = File
    extra = 0


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    """
    Registration of the "Brand" model in the admin panel
    """
    list_display = ['id', 'name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Device)
class AdminDevice(admin.ModelAdmin):
    """
    Registration of the "Device" model in the admin panel
    """
    inlines = [
        FileTabularInline,
    ]
    list_display = ['brand_id', 'name', 'description']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(InstructionFile)
class AdminInstructionFile(admin.ModelAdmin):
    """
    Registration of the "InstructionFile" model in the admin panel
    """
    list_display = ['device_id', 'name', 'description']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(File)
class AdminFile(admin.ModelAdmin):
    """
    Registration of the "File" model in the admin panel
    """

    list_display = ['device_id', 'file_configs', 'file_report']
    list_display_links = ['device_id']


@admin.register(Network)
class AdminNetwork(admin.ModelAdmin):
    """
    Registration of the "Network" model in the admin panel
    """
    list_display = ['name', 'description']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Settings)
class AdminSettings(admin.ModelAdmin):
    """
    Registration of the "Settings" model in the admin panel
    """
    save_on_top = True
    list_display = ['interface', 'device']
    list_display_links = ['interface']
    prepopulated_fields = {'slug': ('interface', 'device')}


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    """
    Registration of the "Project" model in the admin panel
    """
    list_display = ['crm_id', 'company', 'project', 'created_at']
    list_display_links = ['crm_id', 'project']
    prepopulated_fields = {'slug': ('crm_id', 'project')}
