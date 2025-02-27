import os
import re
import logging
import zipfile

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
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
    logger.infor(f"Сформирован slug  для {instance.project}")


@receiver(pre_save, sender=Device)
def get_slugify_settings(instance, **kwargs) -> None:
    """
    Before saving the "Device" model, the "slug" field is checked, if the field is empty,
    it is filled in from the "crm_id", "project" fields of the "Progect" model and the "design"
    fields of the "Device" model via the "slugify" module
    """
    if not instance.slug:
        instance.slug = f"{slugify(instance.project_id.crm_id)}-{slugify(instance.project_id.project)}-{slugify(instance.designation)}"
    logger.infor(f"Сформирован slug  для {instance.project}")


@receiver(post_delete, sender=Project)
@receiver(pre_save, sender=Project)
def cleaned_cache_project(instance, **kwargs) -> None:
    """
    The cache is cleared before saving the "Project" model
    """
    if not instance.slug:
        instance.slug = f"{slugify(instance.crm_id)}-{slugify(instance.project)}"
        logger.info(f"Сформирован slug  для {instance.project}")
    if instance.project:
        instance.project = instance.project.replace(" ", "_")
        logger.info(f"отформатировано имя проекта {instance.project}")
    logger.warning(f"Очищен кеш `{clear_cache(settings.CACHE_NAME_PROJECT)}`")


@receiver(pre_save, sender=Project)
def created_zip_archive(instance, **kwargs) -> None:
    """ """
    try:
        if instance.files.all():
            file_zip = os.path.join(settings.MEDIA_ROOT, f"{instance}.zip")
            dir_path = os.path.join(settings.BASE_DIR, os.path.join(settings.MEDIA_ROOT, os.path.join('files', f'{instance}')))
            files = []
            for root, _, _files in os.walk(dir_path):
                for file in _files:
                    files.append(os.path.join(root, file))
                logger.info("Надены все файлы для архивации в .zip")

            with zipfile.ZipFile(file_zip, "w") as _object:
                for file in files:
                    _object.write(
                        file, compress_type=zipfile.ZIP_DEFLATED
                    )
                logger.info(f"Создан архив с файлами. Имя архива {instance}.zip")

            archive = ArchiveFile.objects.update_or_create(project_id=instance, zip_archive=file_zip)
            if not archive:
                logger.info("Добавлен архив в БД - модель ArchiveFile")
                archive.save()
                logger.info("Сохранены изменения в БД - модель ArchiveFile")
    except Exception as err:
        logger.error(f'Ошибка: {err}')