from django import template
from django.utils.module_loading import cached_import

from instruction.models import InstructionFile, Project

register = template.Library()

@register.filter
def isinst(value, class_str):
    
    class_split = str(InstructionFile).split('.')
    class_name = InstructionFile if class_str in class_split[-1] else Project

    return isinstance(value, class_name)