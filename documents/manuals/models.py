from django.db import models
from django.urls import reverse


def path_to_file_instruction(instance: "FileModule", filename: str) -> str:
    """
    The function generates a path based on the name of the file with the instruction.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"files/{instance.name}/instruction/{filename}"


def path_to_file_manual(instance: "FileModule", filename: str) -> str:
    """
    The function generates a path based on the name of the file with the configs.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"files/{instance.name}/manuals/{filename}"


class Brand(models.Model):
    """
    The class describes the Brand model
    """

    name = models.CharField(max_length=100, verbose_name="Brand", db_index=True)
    slug = models.SlugField(max_length=100, verbose_name="URL", unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "brands"
        verbose_name = "brand"
        verbose_name_plural = "brands"


class Module(models.Model):
    """ """

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand")
    name = models.CharField(max_length=80, verbose_name="Module", db_index=True)
    slug = models.SlugField(max_length=150, verbose_name="URL", unique=True)
    description = models.TextField(verbose_name="Description", blank=True, default=" ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "modules"
        verbose_name = "module"
        verbose_name_plural = "modules"


class Instructions(models.Model):
    """
    The class describes the Instruction model
    """

    device = models.OneToOneField(
        Module, on_delete=models.CASCADE, verbose_name="Device"
    )
    name = models.CharField(max_length=120, verbose_name="Name", db_index=True)
    slug = models.SlugField(max_length=120, verbose_name="URL", unique=True)
    description = models.TextField(verbose_name="Description", blank=True, default=" ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "instructions"
        verbose_name = "instruction"
        verbose_name_plural = "instructions"


class FileModule(models.Model):
    """
    The class describes the InstructionFile model
    """

    device = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        verbose_name="Device",
        related_name="devices_files",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    file_instruction = models.FileField(
        upload_to=path_to_file_instruction, verbose_name="Инструкция", blank=True
    )
    file_manual = models.FileField(
        upload_to=path_to_file_manual, verbose_name="Руководство", blank=True
    )

    def __str__(self) -> str:
        return f"{self.device.name}"

    class Meta:
        db_table = "file_modules"
        verbose_name = "file"
        verbose_name_plural = "files"
