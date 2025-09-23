from django import forms
from .models import ModelFile

class EmailForm(forms.ModelForm):
    class Meta:
        model = ModelFile
        fields = ['file']