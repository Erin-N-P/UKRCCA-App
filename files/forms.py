from django import forms
from .models import newUser


class createUser(forms.Form):
    model = newUser
    widgets = {
        'firstName': forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'form-control',
            'style': 'padding-left: 10px; width: 310px'
        }),
        'secondName': forms.TextInput(attrs={
            'placeholder': 'Second Name',
            'class': 'form-control',
            'style': 'padding-left: 10px; width: 310px'
        }),
        'teamName': forms.TextInput(attrs={
            'placeholder': 'Team Name',
            'class': 'form-control',
            'style': 'padding-left: 10px; width: 310px'
        })
    }
