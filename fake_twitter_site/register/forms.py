from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder':'Password Confirmation','class':'form-control'}))

    class Meta:
        fields = ['username','password1','password2']
        model = User

class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))