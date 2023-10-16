from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",'first_name','last_name','email',)
        field_classes = {'username':UsernameField}
        help_texts = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'password1': None,
            'password2': None,
        }
