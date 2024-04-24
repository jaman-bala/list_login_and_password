from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['title', 'url', 'ip_address', 'login', 'password', 'descriptions']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'url': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ip_address': forms.TextInput(
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
            'descriptions': forms.Textarea(
                attrs={
                    'class': 'form-control', 'rows': 4
                }
            ),
                    }
