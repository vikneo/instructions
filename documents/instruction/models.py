from django.db import models
from django.urls import reverse

# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill


def path_to_file_configs(instance: "FileDevice", filename: str) -> str:
    """
    The function generates a path based on the name of the file with the configs.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"configs/{instance.device_id.name}/{filename}"


def path_to_file_report(instance: "FileProject", filename: str) -> str:
    """
    The function generates a path based on the name of the file with the report.

    :param instance: object File
    :param filename: name file
    :return: str - path to save
    """
    return f"photos/{instance.project_id}/{filename}"


def path_to_file(instance: "FileProject", filename: str) -> str:
    """
    The function generates a path based on the name of the file .

    :param instance: object FileProject
    :param filename: name FileProject
    :return: str - path to save
    """
    return f"files/{instance.project_id}/{filename}"


def path_to_zip_file(instance: "ArchiveFile", filename: str) -> str:
    """
    The function generates a path based on the name of the file .

    :param instance: object ArchiveFile
    :param filename: name file
    :return: str - path to save
    """
    return f"zip_files/{instance.project_id}/{filename}"


class Project(models.Model):
    """
    The class describes the Project model
    """

    crm_id = models.CharField(max_length=10, verbose_name="ID CRM", db_index=True)
    company = models.CharField(max_length=120, verbose_name="Company")
    project = models.CharField(
        max_length=120,
        verbose_name="Project",
    )
    slug = models.SlugField(
        max_length=200, verbose_name="URL", db_index=True, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    description = models.TextField(verbose_name="Info", default=" ", blank=True)
    archive = models.BooleanField(default=False, verbose_name="Archive", blank=True)

    def __str__(self) -> str:
        return f"{self.crm_id}-{self.project}"

    def get_absolute_url(self):
        return reverse("project:product-detail", kwargs={"slug": self.slug})

    class Meta:
        db_table = "project"
        verbose_name = "project"
        verbose_name_plural = "projects"


class Device(models.Model):
    """
    The class describes the Device model
    """

    project_id = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        verbose_name="Project",
        blank=True,
        default="not project",  # type: ignore
    )
    name = models.CharField(max_length=80, verbose_name="Device", db_index=True)
    designation = models.CharField(
        max_length=100, verbose_name="Обозначение", blank=True
    )
    serial_num = models.CharField(
        max_length=25, verbose_name="Serial number", default="n/a", blank=True
    )
    slug = models.SlugField(max_length=150, verbose_name="URL", unique=True)
    description = models.TextField(
        verbose_name="Description", blank=True, default="Пока данных нет"
    )
    termodate = models.BooleanField(default=False, verbose_name="Termo date")
    network_id = models.ManyToManyField("Network", verbose_name="Network")

    def __str__(self) -> str:
        if self.serial_num:
            return f"{self.designation}-{self.serial_num}"
        else:
            return f"{self.name}"

    def get_absolute_url(self):
        return reverse("project:device-detail", kwargs={"slug": self.slug})

    class Meta:
        db_table = "devices"
        verbose_name = "device"
        verbose_name_plural = "devices"


class FileDevice(models.Model):
    """
    The class describes the InstructionFile model
    """

    device_id = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        verbose_name="Device",
        related_name="devices_files",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    file_configs = models.FileField(
        verbose_name="Файлы", upload_to=path_to_file_configs, blank=True
    )
    # file_configs = ProcessedImageField(
    #     upload_to = path_to_file_configs,
    #     verbose_name = 'Photo config',
    #     blank = True,
    #     options={'quantity': 100},
    #     format= 'JPEG',
    #     processors=[ResizeToFill(850, 380)]
    #     )

    def __str__(self) -> str:
        return f"{self.device_id.name}"

    class Meta:
        db_table = "file_device"
        verbose_name = "photo"
        verbose_name_plural = "photos"


class Network(models.Model):
    """
    The class describes the InstructionFile model
    """

    name = models.CharField(max_length=120, verbose_name="Name", db_index=True)
    slug = models.SlugField(max_length=120, verbose_name="URL", unique=True)
    description = models.TextField(verbose_name="Description", blank=True, default=" ")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "networks"
        verbose_name = "network"
        verbose_name_plural = "networks"


class Settings(models.Model):
    """
    The class describes the Settings model
    """

    class Speed(models.IntegerChoices):
        NOT_USED = 0
        S_1200 = 1200, "1200"
        S_2400 = 2400, "2400"
        S_4800 = 4800, "4800"
        S_9600 = 9600, "9600"
        S_19200 = 19200, "19200"
        S_38400 = 38400, "38400"
        S_57600 = 57600, "57600"
        S_115200 = 115200, "115200"

    class Paritet(models.TextChoices):
        NOT_USED = "-"
        EVEN = "E"
        NONE = "N"
        ODD = "O"

    class Bits(models.IntegerChoices):
        NOT_USED = 0
        SEVEN = 7, "7"
        EIGHT = 8, "8"
        NINE = 9, "9"

    class StopBit(models.IntegerChoices):
        NOT_USED = 0
        ONE = 1, "1"
        TWO = 2, "2"

    interface = models.ForeignKey(
        Network, verbose_name="Interface", on_delete=models.CASCADE
    )
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        verbose_name="Device",
        related_name="devices_settings",
    )
    slug = models.SlugField(
        max_length=50, verbose_name="URL", db_index=True, unique=True
    )
    slave_id = models.IntegerField(verbose_name="Slave ID", blank=True, null=True)
    speed = models.IntegerField(verbose_name="Speed", default=0, choices=Speed.choices)
    paritet = models.CharField(
        max_length=1, verbose_name="Paritet", default="-", choices=Paritet.choices
    )
    bit = models.IntegerField(verbose_name="Bits", default=0, choices=Bits.choices)
    stop_bit = models.IntegerField(
        verbose_name="Stop bit", default=0, choices=StopBit.choices
    )
    ip_address = models.CharField(
        max_length=15, verbose_name="IP address", default="not used"
    )
    mask = models.CharField(max_length=15, verbose_name="Mask", default="not used")
    gateway = models.CharField(
        max_length=15, verbose_name="Gateway", default="not used"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    description = models.TextField(verbose_name="Description", default=" ", blank=True)

    def __str__(self) -> str:
        return f"{self.interface} for {self.device}"

    class Meta:
        db_table = "settings"
        verbose_name = "setting"
        verbose_name_plural = "settings"


class WaveSensor(models.Model):
    """
    The class describes the WaveSensor model
    """

    device_id = models.ForeignKey(
        Device, on_delete=models.CASCADE, verbose_name="Binding", related_name="devices"
    )
    name_rkd = models.CharField(
        max_length=15, verbose_name="Desicn to RKD", db_index=True
    )  # обозначение по РКД
    description = models.CharField(
        max_length=80, verbose_name="Name equipment"
    )  # наименование оборудования
    group = models.CharField(max_length=30, verbose_name="Group")  # группа датчиков
    install = models.IntegerField(
        verbose_name="Column install"
    )  # установлено в колонне
    serial_number = models.CharField(
        max_length=30, verbose_name="Serial number"
    )  # серийный номер
    register = models.IntegerField(verbose_name="Register")  # регистр
    temp_warning = models.CharField(
        max_length=3, verbose_name="Temperature warning", default="85"
    )  # Предупреждение
    temp_error = models.CharField(
        max_length=3, verbose_name="Temperature over", default="90"
    )  # Перегрев

    def __str__(self) -> str:
        return f"{self.name_rkd}"

    class Meta:
        db_table = "wavesensors"
        verbose_name = "sensor"
        verbose_name_plural = "sensors"


class FileProject(models.Model):
    """ """

    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name="Проект", related_name="files"
    )
    name = models.CharField(verbose_name="Название", max_length=110, db_index=True)
    file = models.FileField(verbose_name="Файл", upload_to=path_to_file, blank=True)
    file_photos = models.ImageField(
        verbose_name="Photo", upload_to=path_to_file_report, blank=True  # type: ignore
    )
    # file_photos = ProcessedImageField(
    #     upload_to = path_to_file_report,
    #     verbose_name = 'Photo',
    #     blank = True,
    #     options={'quantity': 60},
    #     format= 'JPEG',
    #     processors=[ResizeToFill(310, 280, anchor=False)]
    #     )

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse()  # type: ignore

    class Meta:
        db_table = "file_project"
        verbose_name = "file"
        verbose_name_plural = "files"


class ArchiveFile(models.Model):
    """ """

    pass
    project_id = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Проект",
        related_name="zip_archives",
    )
    zip_archive = models.FileField(
        verbose_name="Zip archive", upload_to=path_to_zip_file, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")

    def __str__(self):
        return f"{self.zip_archive}"

    class Meta:
        db_table = "zip_archives"
        verbose_name = "zip_archive"
        verbose_name_plural = "zip_archives"
