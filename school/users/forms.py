from django import forms
from .models import User, Profile

from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import User

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]


class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = [
            'bio',
            'photo_profile',
            'type_profile'
        ]

        