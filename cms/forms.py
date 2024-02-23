from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LanguageForm(forms.ModelForm):
    class Meta:  
        model = Language 
        exclude = ('created_by',)
        fields = '__all__'
        labels = {
            'lang_name': 'Name',
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", "placeholder":"Username"}))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", "placeholder":"Password"}))