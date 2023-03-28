from django import forms
from django.forms import Select
from .models import *
from django.forms import Select
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
#                 'style': 'padding-left: 10px; width: 600px'
#             }),
#             'first_name': forms.TextInput(attrs={
#                 'placeholder': 'First Name',
#                 'class': 'form-control',
#                 'style': 'padding-left: 10px; width: 600px'
#             }),
#             'last_name': forms.TextInput(attrs={
#                 'placeholder': 'Last Name',
#                 'class': 'form-control',
#                 'style': 'padding-left: 10px; width: 600px'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'placeholder': 'Email',
#                 'class': 'form-control',
#                 'style': 'padding-left: 10px; width: 600px'
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


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 600px'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Location',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 600px'
            }),
            'no_of_rounds': forms.NumberInput(attrs={
                'placeholder': 'No of Rounds',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 600px'
            }),
            'gates_per_round': forms.NumberInput(attrs={
                'placeholder': 'Gates per round',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 600px'
            }),

        }

    def __init__(self, *args, **kwargs):
        super(CompetitionForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['ruleset'].empty_label = "Select Ruleset"


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
        fields = '__all__'
        widgets = {
            'total_score': forms.TextInput(attrs={
                'id': 'scoreFinal',
                'style': 'display: none;'
            }),
            'time_taken': forms.TextInput(attrs={
                'id': 'timeFinal',
                'style': 'display: none;'
            }),
            'round': forms.TextInput(attrs={
                'placeholder': 'Round',
                'id': 'roundFinal',
                'style': 'padding-left: 10px; width: 600px;'
            }),
            'user_id': forms.Select(attrs={'style': 'width:250px'}),
            'comp': forms.Select(attrs={'style': 'width:250px'})

        }

    def __init__(self, *args, **kwargs):
        super(UserScore, self).__init__(*args, **kwargs)
        self.fields['user'].empty_label = "Select User"
        self.fields['total_score'].label = ""
        self.fields['time_taken'].label = ""
        self.fields['user'].label = "User"
        self.fields['comp'].empty_label = "Select Comp"
        self.fields['comp'].label = "Competition"
        self.fields['round'].label = "Round No."
        self.fields['total_score'].label = ""


class RulesetForm(forms.ModelForm):
    class Meta:
        model = Ruleset
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ruleset Name',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 600px'
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
                'style': 'padding-left: 10px; width: 600px'
            }),
            'point': forms.TextInput(attrs={
                'placeholder': 'Number of points',
                'class': 'form-control',
                'style': 'padding-left: 10px; width: 600px'
            }),
        }
