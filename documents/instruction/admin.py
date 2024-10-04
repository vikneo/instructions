from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet

from .models import (
    Brand, 
    Device,
    InstructionFile,
    File,
    Network,
    Settings,
    Project
    )


@admin.action(description='Закрыть доступ')
def close_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(access=False)


@admin.action(description='Открыть доступ')
def open_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(access=True)



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
    list_display = ['brand_id', 'name', 'designation', 'get_id_crm', 'get_company',]
    list_display_links = ['name',]
    prepopulated_fields = {'slug': ('name', 'designation')}
    list_filter = ['name', ]

    def get_id_crm(self, obj):
        if obj.project_set.all():
            return obj.project_set.all()[0]
    
    def get_company(self, obj):
        if obj.project_set.all():
            return obj.project_set.all()[0].company
    
    get_id_crm.short_description = "id crm"
    get_company.short_description = "company"


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
    list_display = ['interface', 'device', 'slave_id']
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
