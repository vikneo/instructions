from django import forms

from .models import InstructionFile


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
