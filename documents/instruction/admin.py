from django.contrib import admin
from .models import (
    Brand, 
    Device,
    InstructionFile,
    File,
    Network,
    Settings
    )


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
    list_display = ['device_id', 'name', 'description']
    list_display_links = ['name']


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
    list_display = ['interface', 'device']
    list_display_links = ['interface']
    prepopulated_fields = {'slug': ('interface', 'device')}

    def interface(self, obj):
        return f"{obj.name}"