from django import forms
from django.core.exceptions import ValidationError

class AddPatientForm(forms.Form):
    full_name = forms.CharField()
    email = forms.CharField()
    phone_no = forms.CharField()
    age = forms.IntegerField()
    patient_id = forms.CharField()
    gender = forms.CharField()