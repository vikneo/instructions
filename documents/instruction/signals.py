from django.dispatch import receiver
from django.db.models.signals import pre_save

from utils.slugify import slugify
from .models import Settings

import re


@receiver(pre_save, sender=Settings)
def get_slugify_instruction(instance, **kwargs) -> None:
    """
    Before saving the model, the "slug" field is checked, 
    if the field is empty, it is filled in from the "name" 
    field through the "slugify" module
    """
    if re.search(r'[0-9]-[0-9]', instance.slug):
        instance.slug = f"{slugify(instance.interface.name)}-{slugify(instance.device.name)}-{slugify(instance.device.designation)}"
                        