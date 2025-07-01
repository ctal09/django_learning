from django import forms

from crud.models import UserInfo
 

class UserDetailForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="First Name")
    last_name = forms.CharField(max_length=30, required=False, label="Last Name")
    email = forms.EmailField(required=False, label="Email")
    dob = forms.IntegerField(required=False, label="Age")
    profile_picture= forms.ImageField(required=False, )
    bio = forms.CharField(required=False,label="bio")
    
    
    class Meta:
        model = UserInfo
        fields = '__all__'
        