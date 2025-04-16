
from django import forms

class CVUploadForm(forms.Form):
    cv = forms.FileField(label="Upload Your CV", required=True)
