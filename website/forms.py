from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class Register(UserCreationForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Enter email-address"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter email-username"}))
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}))
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}))
    
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]