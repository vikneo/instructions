from django.db import models


class Brand:
    """
    The class describes the Brand model
    """
    name = models.CharField(max_length=100, verbose_name='Brand', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='URL')
    device_id = models.ForeignKey("Device", on_delete=models.CASCADE, verbose_name='Device', related_name='devices')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return '/'
    
    class Meta:
        db_table = 'brands'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
    

class Device:
    """
    The class describes the Device model
    """
    name = models.CharField(max_length=150, verbose_name='Device', db_index=True)
    description = models.TextField(verbose_name='Description', blank=True, default=' ')
    slug = models.SlugField(max_length=150, verbose_name='URL')
    files_id = models.ForeignKey("Files", on_delete=models.CASCADE, verbose_name='Photo', related_name='files')
    network_id = models.ForeignKey("Network", on_delete=models.CASCADE, verbose_name='Netork', related_name='networks')
    instruction_file_id = models.OneToOneField("InstructionFile", on_delete=models.CASCADE, verbose_name='Instruction', related_name='instructions')


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'devices'
        verbose_name = 'device'
        verbose_name_plural = 'devices'


class InstructionFile:
    """
    The class describes the InstructionFile model
    """
    name = models.CharField(max_length=120, verbose_name='Name', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL')
    description = models.TextField(verbose_name='Description', blank=True, default=' ')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'instructions'
        verbose_name = 'instruction'
        verbose_name_plural = 'instructions'


class File:
    """
    The class describes the InstructionFile model
    """
    name = models.CharField(max_length=120, verbose_name='Name', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL')
    description = models.TextField(verbose_name='Description', blank=True, default=' ')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'files'
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class Network:
    """
    The class describes the InstructionFile model
    """
    name = models.CharField(max_length=120, verbose_name='Name', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL')
    description = models.TextField(verbose_name='Description', blank=True, default=' ')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'networks'
        verbose_name = 'network'
        verbose_name_plural = 'networks'

# TODO дописать модель Settings - for config Networks
