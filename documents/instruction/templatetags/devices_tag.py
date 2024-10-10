from django import template
from django.http import HttpResponse
from django.core.cache import cache

from instruction.models import Device

register = template.Library()

@register.simple_tag(name='termo_date')
def termo_date(devices=None):
    """
    """
    for dev in devices:
        if dev.termodate:
            return True
