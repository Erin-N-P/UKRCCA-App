from django import forms
from django.forms import ModelForm
from files.models import NewUser

class MyForm(forms.ModelForm):
  class Meta:
    model = NewUser
    fields = ["fName", "sName", "tName", "ctName",]
    labels = {'fName': "First Name:", "sName": "Second Name:", "tName": "Team Name:", "ctName": "Confirm Team Name:",}

    def __init__(self, *args, **kwargs):
      super(MyForm, self).__init__(*args, **kwargs)
      self.fields['fName'].required = True
      self.fields['sName'].required = True
      self.fields['tName'].required = True
      self.fields['ctName'].required = True
