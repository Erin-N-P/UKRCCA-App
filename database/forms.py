from django import forms
from .models import *


class UserForm(forms.ModelForm):

    class Meta:
        model = NewUser
        fields = ('user_name', 'first_name', 'last_name', 'email')
        widgets = {
            'user_name': forms.TextInput(attrs={
                'placeholder': 'User Name',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
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


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Location',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
            'no_of_rounds': forms.NumberInput(attrs={
                'placeholder': 'No of Rounds',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
            'gates_per_round': forms.NumberInput(attrs={
                'placeholder': 'Gates per round',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CompetitionForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = '__all__'
        widgets = {

        }

    def __init__(self, *args, **kwargs):
        super(ScoreForm, self).__init__(*args, **kwargs)
        self.fields['comp'].required = True


class createUser(forms.Form):
    firstName = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': 'First Name...'}))
    secondName = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Second Name..'}))
    teamName = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Team Name...'}))
    
class UserScore(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['user', 'comp']
        widgets = {

        }
    
class RulesetForm(forms.ModelForm):
    class Meta:
        model = Ruleset
        fields = ['name']

