import re
import logging

from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.cache import cache
from django.conf import settings

from utils.slugify import slugify
from utils.log_config import clear_cache
from .models import Settings, Project, InstructionFile


logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Settings)
def get_slugify_settings(instance, **kwargs) -> None:
    """
    Before saving the model, the "slug" field is checked, 
    if the field is empty, it is filled in from the "name" 
    field through the "slugify" module
    """
    if re.search(r'[0-9]-[0-9]', instance.slug):
        instance.slug = f"{slugify(instance.device.name)}-{slugify(instance.device.designation)}-{slugify(instance.device.serial_num)}"

@receiver(pre_save, sender=InstructionFile)
def get_slugify_instruction(instance, **kwargs) -> None:
    """
    Before saving the model, the "slug" field is checked, 
    if the field is empty, it is filled in from the "name" 
    field through the "slugify" module
    """
    if not instance.slug:
        instance.slug = f"{slugify(instance.name)}"

@receiver(pre_save, sender=Project)
def cleaned_cache_project(instance, **kwargs) -> None:
    """
    
    """
    logger.warning(f'Очищен кеш `{clear_cache(settings.CACHE_NAME_PROJECT)}`')


@receiver(pre_save, sender=InstructionFile)
def cleaned_cache_instructions(instance, **kwargs) -> None:
    """
    
    """
    logger.warning(f'Очищен кеш `{clear_cache(settings.CACHE_NAME_INSTRUCT)}`')

