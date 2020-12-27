from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.ModelForm):

    username = forms.CharField(label="Nom")
    password = forms.CharField(label="Mot de pass")

    class Meta:
        model = User
        fields = ('username','password')