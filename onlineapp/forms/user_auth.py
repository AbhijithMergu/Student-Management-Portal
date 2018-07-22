from django import forms

class SignUpForm(forms.Form):
	first_name = forms.CharField(
		max_length=75,
		required= True,
		widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'})
	)

	last_name = forms.CharField(
		max_length=75,
		required=True,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'})
	)

	username = forms.CharField(
		max_length=75,
		required=True,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User Name'})
	)

	password = forms.CharField(
		max_length=25,
		required=True,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
	)


class LoginForm(forms.Form):
	username = forms.CharField(
		max_length=75,
		required=True,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User Name'})
	)

	password = forms.CharField(
		max_length=25,
		required=True,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
	)
