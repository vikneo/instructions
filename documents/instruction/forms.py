from django import forms

from models import WaveSensor


class CSVImportForm(forms.Form):
    """ """

    csv_file = forms.FileField()