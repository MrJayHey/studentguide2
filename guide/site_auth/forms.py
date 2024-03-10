from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required
    fields, plus extra fields for CustomUser.
    """

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'surname', 'study_group', 'password1', 'password2', 'phone', 'is_active', 'is_staff')
        widgets = {
            'email': forms.EmailInput(attrs={'id': 'login', 'name': 'login', 'class': 'input-field'}),
            'study_group': forms.TextInput(attrs={'id': 'group', 'name': 'group', 'placeholder': '221-325', 'class': 'input-field'}),
            'first_name': forms.TextInput(attrs={'id': 'surname2', 'name': 'surname2', 'placeholder': 'Андрей', 'class': 'input-field fullname'}),
            'last_name': forms.TextInput(attrs={'id': 'surname1', 'name': 'surname1', 'placeholder': 'Василиванов', 'class': 'input-field fullname'}),
            'surname': forms.TextInput(attrs={'id': 'surname3', 'name': 'surname3', 'placeholder': 'Игоревич', 'class': 'input-field fullname'}),
            'phone': forms.TextInput(attrs={'id': 'phone', 'name': 'phone', 'placeholder': '+7 1234567890', 'class': 'input-field'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
            'is_active': forms.RadioSelect(attrs={'value':'Я староста', 'name':'role'}),
            'is_staff': forms.RadioSelect(attrs={'value':'Я профорг', 'name':'role'}),
        }
        
        def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            self.fields['surname'].required = False
            
            
        
class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'study_group')
