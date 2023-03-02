from django import forms
from django.db import models
from .models import *


class createUser(forms.Form):
    firstName = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': 'First Name...'}))
    secondName = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Second Name..'}))
    teamName = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Team Name...'}))
