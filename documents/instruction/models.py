from django.db import models


class Brand(models.Model):
    """
    The class describes the Brand model
    """
    name = models.CharField(max_length=100, verbose_name='Brand', db_index=True)
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)

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
    slug = models.SlugField(max_length=150, verbose_name='URL', unique=True)
    description = models.TextField(verbose_name='Description', blank=True, default=' ')
    device_id = models.ManyToManyField("Network", verbose_name='Netork')


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
    slug = models.SlugField(max_length=120, verbose_name='URL', unique=True)
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
    name = models.CharField(max_length=120, verbose_name='Name', db_index=True)
    slug = models.SlugField(max_length=120, verbose_name='URL', unique=True)
    description = models.TextField(verbose_name='Description', blank=True, default=' ')

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
    class Speed(models.IntegerChoices):
        NOT_USED = 0
        S_1200 = 1200, '1200'
        S_2400 = 2400, '2400'
        S_4800 = 4800, '4800'
        S_9600 = 9600, '9600'
        S_19200 = 19200, '19200'
        S_38400 = 38400, '38400'
        S_57600 = 57600, '57600'
        S_115200 = 115200, '115200'

    class Paritet(models.TextChoices):
        NOT_USED = '-'
        EVEN = 'E'
        NONE = 'N'
        ODD = 'O'
    
    class Bits(models.IntegerChoices):
        NOT_USED = 0
        SEVEN = 7, '7'
        EIGHT = 8, '8'
        NINE = 9, '9'
    
    class StopBit(models.IntegerChoices):
        NOT_USED = 0
        ONE = 1, '1'
        TWO = 2, '2'

    interface = models.ForeignKey(Network, verbose_name='Interface', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='Device', related_name='devices_settings')
    slug = models.SlugField(max_length=50, verbose_name='URL', db_index=True, unique=True)
    slave_id = models.IntegerField(verbose_name='Slave ID', blank=True, null=True)
    speed = models.IntegerField(verbose_name='Speed', default=0, choices=Speed.choices)
    paritet = models.CharField(max_length=1, verbose_name='Paritet', default='-', choices=Paritet.choices)
    bit = models.IntegerField(verbose_name='Bits', default=0, choices=Bits.choices)
    stop_bit = models.IntegerField(verbose_name='Stop bit', default=0, choices=StopBit.choices)
    ip_address = models.CharField(max_length=15, verbose_name='IP address', default='not used')
    mask = models.CharField(max_length=15, verbose_name='Mask', default='not used')
    gateway = models.CharField(max_length=15, verbose_name='Gateway', default='not used')
    description = models.TextField(verbose_name='Description', default=' ', blank=True)

    def __str__(self) -> str:
        return f"{self.interface} for {self.device}"
    
    class Meta:
        db_table = 'settings'
        verbose_name = 'setting'
        verbose_name_plural = 'settings'