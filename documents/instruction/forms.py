from django import forms

from .models import InstructionFile, Device


class CSVImportForm(forms.Form):
    """ """

    csv_file = forms.FileField()


class CreatedInstructionForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["brand_id"].empty_label = "Производители"
        self.fields["device_id"].empty_label = "Устройство"

    name = forms.CharField(
        label="Название",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "name",
                "name": "name",
                "type": "text",
                "data-validate": "require",
            }
        ),
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "description",
                "name": "description",
                "type": "text",
                "data-validate": "require",
            }
        ),
    )
    docs = forms.FileField(label="Файл")

    class Meta:
        model = InstructionFile
        fields = ["brand_id", "device_id", "name", "description", "docs"]


class CreatedDeviceForm(forms.ModelForm):
    """
    
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["brand_id"].empty_label = "Производители"
        self.fields["project_id"].empty_label = "Проекты"
    
    name = forms.CharField(
        label='Наименование', 
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "name",
                "name": "name",
                "type": "text",
                "data-validate": "require",                
            }
            ))
    designation = forms.CharField(
        label='Обозначение по РКД',
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "designation",
                "name": "designation",
                "type": "text",
                "data-validate": "require",
            }
        )
    )
    serial_num = forms.CharField(
        label='Серийный номер',
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "serial_num",
                "name": "serial_num",
                "type": "text",
                "data-validate": "require",
            }
        )
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'row': 60,
                'cols': 5,
                "class": "form-input",
                "id": "description",
                "name": "description",
                "type": "text",
                "data-validate": "require",
            }
        )
    )
    termodate = forms.CharField(label='Термомониторинг', widget=forms.CheckboxInput())

    class Meta:
        model = Device
        fields = [
            'brand_id',
            'project_id',
            'name',
            'designation',
            'serial_num',
            'description',
            'termodate',
            'network_id'
        ]
