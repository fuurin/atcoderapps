from django import forms

class UserNamesForm(forms.Form):
	username = forms.CharField(required=True)
	rivalname = forms.CharField(required=False)

	def set_attr(self, field_name, attrs):
		self.fields[field_name].widget.attrs.update(attrs)