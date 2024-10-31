from django import template

register = template.Library()


@register.simple_tag(name = 'termo_date')
def termo_date(devices = None):
    """
    """
    for dev in devices:
        if dev.termodate:
            return True
