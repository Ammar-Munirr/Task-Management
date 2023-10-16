from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model
from .models import Tasks

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",'first_name','last_name','email',)
        field_classes = {'username':UsernameField}
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Enter Username:'}),
            'first_name':forms.TextInput(attrs={'placeholder':'Enter First Name:'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name:'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter your E-Mail:'}),
            
        }
        help_texts = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'password1': None,
            'password2': None,
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title','description','due_date']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Enter Title:'}),
            'description':forms.Textarea(attrs={'placeholder':'Enter Description:'}),
            'due_date':forms.DateInput(attrs={'type': 'date','placeholder':'Enter Task Due Date'})
        }