from django import template
from django.http import HttpResponse
from django.core.cache import cache

from instruction.models import FileProject

register = template.Library()


@register.simple_tag(name="photos_device")
def photos_device(project_id):
    """ """
    devices = FileProject.objects.filter(project_id=project_id)

    photos = [dev.file_photos for dev in devices]
    # for dev in devices:
    #     print(dev.file_photos)
    # for photo in dev.file_photos:
    #     photos.append(photo)

    return photos
