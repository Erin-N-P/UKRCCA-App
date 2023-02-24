from django import forms
from .models import NewUser

class UserForm(forms.ModelForm):

    class Meta:
        model = NewUser
        fields = ('user_name','first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['email'].disabled = True
        self.fields['user_name'].required = True
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 