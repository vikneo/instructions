from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet
from import_export.admin import ImportExportModelAdmin

from .models import (
    Brand, 
    Device,
    InstructionFile,
    File,
    Network,
    Settings,
    Project,
    WaveSensor
    )


@admin.action(description='Del Termo date')
def close_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(termodate=False)


@admin.action(description='Add Termo date')
def open_access(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(termodate=True)



class FileTabularInline(admin.TabularInline):
    model = File
    extra = 0


@admin.register(Brand)
class AdminBrand(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Registration of the "Brand" model in the admin panel
    """
    list_display = ['id', 'name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Device)
class AdminDevice(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Registration of the "Device" model in the admin panel
    """
    inlines = [
        FileTabularInline,
    ]
    actions = [
        close_access,
        open_access
    ]
    list_display = ['id', 'name', 'serial_num', 'designation', 'termodate', 'get_id_crm', 'get_project',]
    list_display_links = ['name',]
    prepopulated_fields = {'slug': ('name', 'designation')}
    list_filter = ['name', 'serial_num']

    def get_id_crm(self, obj):
        return obj.project_id
    
    def get_project(self, obj):
        return obj.project_id.company
    
    get_id_crm.short_description = "id / project"
    get_project.short_description = "company"


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
class AdminNetwork(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Registration of the "Network" model in the admin panel
    """
    list_display = ['name', 'description']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Settings)
class AdminSettings(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Registration of the "Settings" model in the admin panel
    """
    save_on_top = True
    list_display = ['interface', 'device', 'slave_id']
    list_display_links = ['interface']
    prepopulated_fields = {'slug': ('interface', 'device')}


@admin.register(Project)
class AdminProject(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Registration of the "Project" model in the admin panel
    """
    list_display = ['crm_id', 'company', 'project', 'created_at']
    list_display_links = ['crm_id', 'project']
    prepopulated_fields = {'slug': ('crm_id', 'project')}


@admin.register(WaveSensor)
class AdminWaveSensor(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Registration of the "AdminWaveSensor" model in the admin panel
    """
    list_display = ['id', 'get_id_crm', 'get_project', 'device_id', 'name_rkd']
    list_display_links = ['name_rkd',]
    list_filter = ['device_id',]
    ordering = ['id']

    def get_project(self, obj) -> str:
        id_project = obj.device_id.project_set.first()
        if id_project:
            return id_project.project
    
    def get_id_crm(self, obj) -> str:
        return obj.device_id.project_set.first()
    
    get_project.short_description = 'project'
    get_id_crm.short_description = 'id-crm'
