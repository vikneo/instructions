from django import forms

from .models import Device, Project, FileProject


class CSVImportForm(forms.Form):
    """ """

    csv_file = forms.FileField()


class AddFileForm(forms.ModelForm):
    """
    
    """
    file = forms.FileField(label='Файлы проекта')

    class Meta:
        model = FileProject
        fields = ['file']


class CreatedDeviceForm(forms.ModelForm):
    """
    
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["project_id"].empty_label = "Выбрать проект"
        self.fields['serial_num'].required = False
        self.fields['description'].required = False
        self.fields['network_id'].required = False
    
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
                'cols': 10,
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
            'project_id',
            'name',
            'designation',
            'serial_num',
            'description',
            'termodate',
            'network_id'
        ]


class CrerateprojectForm(forms.ModelForm):
    """
    
    """
    crm_id = forms.CharField(
        label='ID_CRM',
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "crm_id",
                "name": "crm_id",
                "type": "text",
                "data-validate": "require",
            }
        )
    )
    company = forms.CharField(
        label='Заказчик',
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "company",
                "name": "company",
                "type": "text",
                "data-validate": "require",
            }
        )
    )
    project = forms.CharField(
        label='Проект',
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "id": "project",
                "name": "project",
                "type": "text",
                "data-validate": "require",
            }
        )
    )
    description = forms.CharField(
        label='Дополнительно',
        required=False,
        widget=forms.Textarea(
            attrs={
                # 'row': 5,
                # 'cols': 60,
                "class": "form-text",
                "id": "description",
                "name": "description",
                "type": "text",
                "data-validate": "require",
            }
        )
    )

    class Meta:
        model = Project
        fields = [
            'crm_id',
            'company',
            'project',
            'description'
        ]
