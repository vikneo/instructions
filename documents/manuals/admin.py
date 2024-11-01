import logging

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import Brand, Module, FileModule

logger = logging.getLogger(__name__)



@admin.register(Brand)
class AdminBrand(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Registration of the "Brand" model in the admin panel
    """
    list_display = ['id', 'name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}



class FileTabularInline(admin.TabularInline):
    model = FileModule
    extra = 0


@admin.register(Module)
class AdminModule(admin.ModelAdmin):
    """
    
    """
    inlines = [
        FileTabularInline,
    ]
    
    list_display = ['name', 'brand', 'description']
    list_filter = ['name']
    search_fields = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FileModule)
class AdminFileModule(admin.ModelAdmin):
    """
    Registration of the "File" model in the admin panel
    """

    list_display = ['device', 'file_instruction', 'file_manual']
    list_display_links = ['device']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
            logger.info(f"`{request.user}` добавил {obj} в модель {self.model.__name__}")
        obj.save()

