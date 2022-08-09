from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Ismingiz',
            'email': 'Elektron hat',
            'username': 'Nikingiz',
            'password1': 'Parol',
            'password2': 'Parolni taskdiqlash'
        }