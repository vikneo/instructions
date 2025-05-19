from django import template

from instruction.models import Project


register = template.Library()


@register.simple_tag(name="termo_date")
def termo_date(devices = None):
    """
    """
    for dev in devices:
        if dev.termodate:
            return True


@register.simple_tag(name="project_breadcrumb")
def project_breadcrumb(slug):
    """ """
    print(slug)
    project = Project.objects.get(slug=slug)
    print(project)
    return project
