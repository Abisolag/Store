from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserResigrationForm(UserCreationForm):
    email =forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image',]

class UserCheckForm(forms.ModelForm):
    class Meta:
        model = Usercheckout
        fields = "__all__"