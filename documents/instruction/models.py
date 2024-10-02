from django.db import models


class Brand(models.Model):
    """
    The class describes the Brand model
    """
    name = models.CharField(max_length=100, verbose_name='Brand', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='URL')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return '/'
    
    class Meta:
        db_table = 'brands'
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
    

class Device(models.Model):
    """
    The class describes the Device model
    """
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Device', related_name='brands')
    name = models.CharField(max_length=150, verbose_name='Device', db_index=True)
    slug = models.SlugField(max_length=150, verbose_name='URL')
    description = models.TextField(verbose_name='Description', blank=True, default=' ')


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'devices'
        verbose_name = 'device'
        verbose_name_plural = 'devices'


class InstructionFile(models.Model):
    """
    The class describes the InstructionFile model
    """
    device_id = models.OneToOneField(Device, on_delete=models.CASCADE, verbose_name='Instruction', related_name='devices_instructs')
    name = models.CharField(max_length=120, verbose_name='Name', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL')
    description = models.TextField(verbose_name='Description', blank=True, default=' ')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'instructions'
        verbose_name = 'instruction'
        verbose_name_plural = 'instructions'


class File(models.Model):
    """
    The class describes the InstructionFile model
    """
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='Photo', related_name='devices_files')
    name = models.CharField(max_length=120, verbose_name='Name', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL')
    description = models.TextField(verbose_name='Description', blank=True, default=' ')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'files'
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class Network(models.Model):
    """
    The class describes the InstructionFile model
    """
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='Netork', related_name='devices_networks')
    name = models.CharField(max_length=120, verbose_name='Name', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL')
    description = models.TextField(verbose_name='Description', blank=True, default=' ')
    settings = models.OneToOneField("Settings", verbose_name="Settings", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'networks'
        verbose_name = 'network'
        verbose_name_plural = 'networks'


class Settings(models.Model):
    """
    The class describes the Settings model
    """
    class Speed(models.TextChoices):
        '1200'
        '2400'
        '4800'
        '9600'
        '19200'
        '38400'
        '57600'
        '115200'

        __empty__ = 'speed'

    class Paritet(models.TextChoices):
        EVEN = 'E'
        NONE = 'N'
        ODD = 'O'

        __empty__ = 'paritet'
    
    class Bits(models.TextChoices):
        '7'
        '8'
        '9'

        __empty__ = 'bits'
    
    class StopBit(models.TextChoices):
        '1'
        '2'

        __empty__ = 'storp bits'

    mode = models.CharField(max_length=50, verbose_name='Mode', db_index=True)
    slug = models.SlugField(max_length=50, verbose_name='URL', db_index=True)
    slave_id = models.IntegerField(verbose_name='Slave ID')
    speed = models.CharField(max_length=6, verbose_name='Speed', default='9600', choices=Speed)
    paritet = models.CharField(max_length=1, verbose_name='Paritet', default='N', choices=Paritet)
    bit = models.CharField(max_length=1, verbose_name='Bits', default='8', choices=Bits)
    stop_bit = models.CharField(max_length=1, verbose_name='Stop bit', default='1', choices=StopBit)
    ip_address = models.CharField(max_length=15, verbose_name='IP address')
    mask = models.CharField(max_length=15, verbose_name='Mask')
    gateway = models.CharField(max_length=15, verbose_name='Gateway')
    description = models.TextField(verbose_name='Description', default=' ', blank=True)

    def __str__(self) -> str:
        return self.mode
    
    class Meta:
        db_table = 'settings'
        verbose_name = 'setting'
        verbose_name_plural = 'settings'