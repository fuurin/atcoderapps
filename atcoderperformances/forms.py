from django import forms

class UserNameForm(forms.Form):
	username = forms.CharField(required=True)