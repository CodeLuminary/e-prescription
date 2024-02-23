from django import forms
from django.core.exceptions import ValidationError

class AddDrugForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()