from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from .models import Brand



@admin.register(Brand)
class AdminBrand(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Registration of the "Brand" model in the admin panel
    """
    list_display = ['id', 'name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}



# class FileTabularInline(admin.TabularInline):
#     model = File
#     extra = 0

# @admin.register(InstructionFile)
# class AdminInstructionFile(admin.ModelAdmin):
#     """
#     Registration of the "InstructionFile" model in the admin panel
#     """
#     list_display = ['brand_id', 'device_id', 'name', 'description']
#     list_display_links = ['name']
#     prepopulated_fields = {'slug': ('name',)}

#     def save_model(self, request, obj, form, change):
#         if getattr(obj, 'creator', None) is None:
#             obj.creator = request.user
#             logger.info(f"`{request.user}` добавил {obj} в модель {self.model.__name__}")
#         obj.save()


# @admin.register(File)
# class AdminFile(admin.ModelAdmin):
#     """
#     Registration of the "File" model in the admin panel
#     """

#     list_display = ['device_id', 'file_configs', 'file_report']
#     list_display_links = ['device_id']

#     def save_model(self, request, obj, form, change):
#         if getattr(obj, 'creator', None) is None:
#             obj.creator = request.user
#             logger.info(f"`{request.user}` добавил {obj} в модель {self.model.__name__}")
#         obj.save()

