from django import forms
from onlineapp.models import College


class AddCollege(forms.ModelForm):
	class Meta:
		model = College
		exclude = ['id']

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
			'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
			'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter acronym'}),
			'contact': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Email'}),
		}
