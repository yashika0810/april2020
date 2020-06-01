from django import forms
from django.core import validators
from django.forms import ModelForm
from .models import Login


class Loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"


 








# def check(value):
#     if len(value) < 6:
#         raise forms.ValidationError("Please provide more than 6 characters")

# def check(value):
#     if value[0].lower() != 'a':
#         raise forms.ValidationError("Name should start with a")


#    def clean(self):
#         email=self.cleaned_data['email']
#         vemail=self.cleaned_data['verify_email']
#         if email!=vemail:
#             raise forms.ValidationError("Your email don't match")


 




