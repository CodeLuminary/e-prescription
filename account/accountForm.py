from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    user_type = forms.CharField()