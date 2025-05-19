from django import template

# from django.utils.module_loading import cached_import
from instruction.models import Project
from manuals.models import Instructions

register = template.Library()


@register.filter
def isinst(value, class_str):
    class_split = str(Instructions).split(".")
    class_name = Instructions if class_str in class_split[-1] else Project
    return isinstance(value, class_name)
