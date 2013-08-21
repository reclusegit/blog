from django import forms

class UserForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)


class IssueRecord(forms.Form):
	issueName = forms.CharField(max_length = 100)
	solution  = forms.CharField(max_length = 100)
	qq = forms.CharField(max_length = 20)
	phone = forms.CharField(max_length = 20)