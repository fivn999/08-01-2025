from django import forms
from .models import Contato, User


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'senha']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome','email', 'senha']

