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
