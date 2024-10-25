from django.db import models
from django.urls import reverse

from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit


def path_to_file_instruction(instance: 'Instructions', filename: str) -> str:
    """
    The function generates a path based on the name of the file with the instruction.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"instruction/{instance.name}/{filename}"

def path_to_icon_brand(instance: 'Brand', filename: str) -> str:
    """
    The function generates a path based on the name of the file with the report.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"icon/{instance.name}/{filename}"



class Brand(models.Model):
    """
    The class describes the Brand model
    """
    name = models.CharField(max_length = 100, verbose_name = 'Brand', db_index = True)
    slug = models.SlugField(max_length = 100, verbose_name = 'URL', unique = True)
    icon = ProcessedImageField(
        blank=True,
        verbose_name="Logo",
        upload_to=path_to_icon_brand,
        options={"quality": 80},
        processors=[ResizeToFit(200, 155, mat_color='white')],
        null=True
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('project:index')

    class Meta:
        db_table = 'brands'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'



    # brand_id = models.ForeignKey(Brand, on_delete = models.CASCADE, verbose_name = 'Brand', related_name = 'brands')


class Module(models.Model):
    pass


class Instructions(models.Model):
    """
    The class describes the InstructionFile model
    """
    brand_id = models.ForeignKey(Brand, on_delete = models.CASCADE, verbose_name = 'Brand')
    device_id = models.OneToOneField(Module, on_delete=models.CASCADE, verbose_name='Device')
    name = models.CharField(max_length = 120, verbose_name = 'Name', db_index = True)
    slug = models.SlugField(max_length = 120, verbose_name = 'URL', unique = True)
    description = models.TextField(verbose_name = 'Description', blank = True, default = ' ')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "Date created")
    updated_at = models.DateTimeField(auto_now = True, verbose_name = "Date updated")
    docs = models.FileField(upload_to = path_to_file_instruction, verbose_name = 'File')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('project:instructions')

    class Meta:
        db_table = 'instructions'
        verbose_name = 'instruction'
        verbose_name_plural = 'instructions'


class UserGuide(models.Model):
    pass