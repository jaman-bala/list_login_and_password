from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'contact', 'email', 'title', 'login', 'password', 'descriptions']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'contact': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'login': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descriptions': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
                    }
