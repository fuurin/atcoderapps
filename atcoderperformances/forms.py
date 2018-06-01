from django import forms

class UserNamesForm(forms.Form):
	username = forms.CharField(required=True)
	rivalname = forms.CharField(required=False)