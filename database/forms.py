from django import forms
from .models import NewUser

class UserForm(forms.ModelForm):

    class Meta:
        model = NewUser
        fields = ('user_name','first_name', 'last_name', 'email')
        widgets = {
            'user_name': forms.TextInput(attrs={
            'placeholder':'User Name',
            'class':'form-control',
            'style':'padding-left: 10px; width: 310px'
            }),
            'first_name': forms.TextInput(attrs={
            'placeholder':'First Name',
            'class':'form-control',
            'style':'padding-left: 10px; width: 310px'
            }),
            'last_name': forms.TextInput(attrs={
            'placeholder':'Last Name',
            'class':'form-control',
            'style':'padding-left: 10px; width: 310px'
            }),
            'email': forms.EmailInput(attrs={
            'placeholder':'Email',
            'class':'form-control',
            'style':'padding-left: 10px; width: 310px'
            })
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['email'].disabled = True
        self.fields['user_name'].required = True
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 