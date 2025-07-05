from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User, Profile

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'lastname',
            'password1',
            'password2'
        ]


class Profile(forms.ModelForm):
    class Meta():
        model = Profile
        fields = [
            'bio',
            'photo_profile',
            'type_profile'
        ]

        