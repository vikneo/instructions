import logging

from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from utils.log_config import clear_cache
from utils.slugify import slugify

from .models import Instructions

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Instructions)
def get_slugify_instruction(instance, **kwargs) -> None:
    """
    Before saving the model, the "slug" field is checked,
    if the field is empty, it is filled in from the "name"
    field through the "slugify" module
    """
    if not instance.slug:
        instance.slug = f"{slugify(instance.name)}"


@receiver(pre_save, sender=Instructions)
def cleaned_cache_instructions(instance, **kwargs) -> None:
    """ """
    logger.warning(f"Очищен кеш `{clear_cache(settings.CACHE_NAME_INSTRUCT)}`")
