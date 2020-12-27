from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserCreationForms(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField(label='Nom')
    last_name = forms.CharField(label='Prenom')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mot de pass',widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirme zvotre mot de pass',widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')




class LoginForm(forms.ModelForm):

    username = forms.CharField(label="Nom")
    password = forms.CharField(label="Mot de pass")

    class Meta:
        model = User
        fields = ('username','password')