from django import forms
from .models import *
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)


# class UserForm(forms.ModelForm):

#     class Meta:
#         model = NewUser
#         fields = ('user_name', 'first_name', 'last_name', 'email')
#         widgets = {
#             'user_name': forms.TextInput(attrs={
#                 'placeholder': 'User Name',
#                 'class': 'form-control',
#                 'style': 'padding-left: 10px; width: 310px'
#             }),
#             'first_name': forms.TextInput(attrs={
#                 'placeholder': 'First Name',
#                 'class': 'form-control',
#                 'style': 'padding-left: 10px; width: 310px'
#             }),
#             'last_name': forms.TextInput(attrs={
#                 'placeholder': 'Last Name',
#                 'class': 'form-control',
#                 'style': 'padding-left: 10px; width: 310px'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'placeholder': 'Email',
#                 'class': 'form-control',
#                 'style': 'padding-left: 10px; width: 310px'
#             })
#         }

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = NewUser
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = NewUser.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if NewUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})

    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['email'].disabled = True
    #     self.fields['user_name'].required = True
    #     self.fields['first_name'].required = True
    #     self.fields['last_name'].required = True


class ScoreForm(forms.ModelForm):

    total_time = forms.CharField(
        label='Total Time', min_length=4, max_length=50, help_text='Required')
    total_score = forms.IntegerField(help_text='Required', error_messages={
        'required': 'Please check if you have the right value'})
    user = forms.ChoiceField(
        label='Choose user', widget=forms.Select(attrs={}))
    competition = forms.ChoiceField(
        label='Choose competition', widget=forms.Select(attrs={}))
    round = forms.ChoiceField(label='Choose which round')

    class Meta:
        model = Score
        fields = ('total_score', 'time_taken', 'user', 'comp')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['total_time'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Total Time'})
        self.fields['total_score'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Total Score'})
        self.fields['user'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Choose User'})
        self.fields['comp'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Choose Competition'})


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
        fields = ['user', 'comp', 'total_score', 'time_taken']
        widgets = {
            'total_score': forms.TextInput(attrs={
                'placeholder': 'Final Score',
                'id': 'scoreFinal',
                'style': 'padding-left: 10px; width: 310px'
            }),
            'time_taken': forms.TextInput(attrs={
                'placeholder': 'Final Time',
                'id': 'timeFinal',
                'style': 'padding-left: 10px; width: 310px'
            }),



        }


class RulesetForm(forms.ModelForm):
    class Meta:
        model = Ruleset
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ruleset Name',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
        }


class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Rule Name',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
            'point': forms.TextInput(attrs={
                'placeholder': 'Number of points',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 310px'
            }),
        }
