from django import forms
from .models import Todo

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
class CustomUserCreationForm(UserCreationForm):
    # Override the default fields
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'PASSWORD'}),
        help_text=None,  # Removes help text
        error_messages={'required': ''}  # Removes error message
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'CONFIRM PASSWORD'}),
        help_text=None,  # Removes help text
        error_messages={'required': ''}  # Removes error message
    )
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'USERNAME'}),
        help_text=None,  # Removes help text
        error_messages={'required': ''}  # Removes error message
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']