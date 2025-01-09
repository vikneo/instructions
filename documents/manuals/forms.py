from django import forms

from .models import Instructions


class CreatedInstructionForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["brand"].empty_label = "Производители"
        self.fields["device"].empty_label = "Устройство"

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
        model = Instructions
        fields = ["brand", "device", "name", "description", "docs"]

