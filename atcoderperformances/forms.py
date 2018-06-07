from django import forms

class UserNamesForm(forms.Form):
	username = forms.CharField(required=True)
	rivalname = forms.CharField(required=False)

	def set_username_value(self, name):
		self.fields["username"].widget.attrs.update({"value": name})

	def set_rivalname_value(self, name):
		self.fields["rivalname"].widget.attrs.update({"value": name})