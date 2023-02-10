from django import forms
from .models import NewUser

class UserForm(forms.ModelForm):

    class Meta:
        model = NewUser
        fields = ('first_name', 'last_name', 'email')