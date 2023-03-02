from django import forms


class newUser():
    firstName = forms.CharField(max_length=30)
    secondName = forms.CharField(max_length=30)
    teamName = forms.CharField(max_length=30)

    REQUIRED_FIELDS = ['firstName', 'secondName', 'teamName']
