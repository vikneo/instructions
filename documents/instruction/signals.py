import os
import re
import logging
import zipfile

from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.cache import cache
from django.conf import settings

from utils.slugify import slugify
from utils.log_config import clear_cache
from .models import Settings, Project, Device, ArchiveFile


logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Settings)
def get_slugify_settings(instance, **kwargs) -> None:
    """
    Before saving the "Settings" model, the "slug" field is checked, by default,
    the numerical result from the dependent models is recorded in the slug,
    if any, it is filled in from the "crm_id", "project" fields of the "Progect" model and
    the "design" fields of the "Device" model via the "slugify" module
    """
    result = re.search(r"[0-9]-[0-9]", instance.slug)
    if result:
        instance.slug = f"{slugify(instance.device.project_id.crm_id)}-{slugify(instance.device.project_id.project)}-{slugify(instance.device.designation)}"


@receiver(pre_save, sender=Device)
def get_slugify_settings(instance, **kwargs) -> None:
    """
    Before saving the "Device" model, the "slug" field is checked, if the field is empty,
    it is filled in from the "crm_id", "project" fields of the "Progect" model and the "design"
    fields of the "Device" model via the "slugify" module
    """
    if not instance.slug:
        instance.slug = f"{slugify(instance.project_id.crm_id)}-{slugify(instance.project_id.project)}-{slugify(instance.designation)}"


@receiver(pre_save, sender=Project)
def cleaned_cache_project(instance, **kwargs) -> None:
    """
    The cache is cleared before saving the "Project" model
    """
    if not instance.slug:
        instance.slug = f"{slugify(instance.crm_id)}-{slugify(instance.project)}"
    logger.warning(f"Очищен кеш `{clear_cache(settings.CACHE_NAME_PROJECT)}`")


@receiver(pre_save, sender=Project)
def created_zip_archive(instance, **kwargs) -> None:
    """ """
    file_zip = f"{settings.MEDIA_ROOT}/{instance}.zip"  
    with zipfile.ZipFile(file_zip, "w") as _object:
        for file in instance.files.all():
            _object.writestr(
                str(file.file), "utf-8", compress_type=zipfile.ZIP_DEFLATED
            )

    archive = ArchiveFile.objects.update_or_create(project_id=instance, zip_archive=file_zip)
    if not archive:
        archive.save()
