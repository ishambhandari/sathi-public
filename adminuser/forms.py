from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin

# a class which act as a view - it displays the login-form
class LoginForm(AuthenticationForm, AccessMixin):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
