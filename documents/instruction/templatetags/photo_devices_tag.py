from django import template
from django.http import HttpResponse
from django.core.cache import cache

from instruction.models import Device, Project

register = template.Library()


@register.simple_tag(name = 'photos_device')
def photos_device(project_id):
    """

    """
    photos = []
    devices = Device.objects.filter(project_id=project_id)

    for dev in devices:
        for photo in dev.devices_files.all():
            photos.append(photo)

    return photos