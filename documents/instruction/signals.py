from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.cache import cache

from utils.slugify import slugify
from .models import Settings, Project

import re
import logging

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Settings)
def get_slugify_instruction(instance, **kwargs) -> None:
    """
    Before saving the model, the "slug" field is checked, 
    if the field is empty, it is filled in from the "name" 
    field through the "slugify" module
    """
    if re.search(r'[0-9]-[0-9]', instance.slug):
        instance.slug = f"{slugify(instance.device.name)}-{slugify(instance.device.designation)}-{slugify(instance.device.serial_num)}"
                        

@receiver(pre_save, sender=Project)
def cleaned_cache(instance, **kwargs) -> None:
    """
    
    """
    cache.delete('products')
    logger.warning('Очищен кеш `Project`')

