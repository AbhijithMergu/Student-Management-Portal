from django import forms
from onlineapp.models import Student,MockTest1


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ['id', 'dob', 'college']

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter name'}),
			'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
			'db_folder': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter folder name'}),
			'dropped_out': forms.CheckboxInput(attrs={'class':'checkbox'}),
		}


class MockTestForm(forms.ModelForm):
	class Meta:
		model = MockTest1
		fields = [
			'problem1',
			'problem2',
			'problem3',
			'problem4'
		]
		widgets = {
			'problem1': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Problem1 Score'}),
			'problem2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Problem2 Score'}),
			'problem3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Problem3 Score'}),
			'problem4': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Problem4 Score'}),
		}
