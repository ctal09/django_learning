from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
import datetime

from users.models import User

class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, label="First Name")
    last_name = forms.CharField(max_length=30, required=False, label="Last Name")
    id_name=forms.IntegerField(required=False, label="ID Name")
    email = forms.EmailField(required=False, label="Email")

class FormTwo(forms.Form):
    first_name = forms.CharField(max_length=30, required=False, label="First Name")
    last_name = forms.CharField(max_length=30, required=False, label="Last Name")
    email = forms.EmailField(required=False, label="Email")
    age = forms.IntegerField(required=False, label="Age" )
    address = forms.CharField(max_length=100, required=False, label="Address")
    
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 20 or age > 100:
            raise forms.ValidationError("Age must be between 20 and 100.")
        return age
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must end with '@example.com'.")
        return email

class UserModelForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="First Name")
    last_name = forms.CharField(max_length=30, required=False, label="Last Name")
    email = forms.EmailField(required=False, label="Email")
    age = forms.IntegerField(required=False, label="Age")
    is_active = forms.BooleanField(required=False, label="Is Active")
    # address = forms.CharField(max_length=100, required=False, label="Address")
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None or age < 16:

            raise ValidationError("You must be older than 16")
        return age
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@merojob.com'):
            raise ValidationError("Email must end with '@merojob.com'.")
        return email
    
    # def clean_address(self):
    #     address = self.cleaned_data.get('address')
    #     if not address:
    #         raise ValidationError("Address is required.")
    #     return address
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'age', 'is_active',]
        
        
        
