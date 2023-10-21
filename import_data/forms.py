# import_data/forms.py
from django import forms

class ExcelFileUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')
