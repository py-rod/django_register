from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Task


class UserCreationForm(UserCreationForm):
    email = forms.EmailInput()
    class Meta:
       model = User
       fields = ["username", "email", "password1", "password2"]
       labels = {
           "email": "Email"
       }
       widgets = {
           "username": forms.TextInput(attrs={"class": "username_input"}),
           "email": forms.EmailInput(attrs={"class": "email_input", "required": True})
       }
       
class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(),
            "description": forms.Textarea()
        }