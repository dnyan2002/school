from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'profile_picture', 'date_of_birth', 'skills', 'education']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'profile_picture':forms.FileInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control'}),
            'skills':forms.CheckboxSelectMultiple(attrs={'class':'form-checkbox'}),
            'education':forms.TextInput(attrs={'class':'form-control'}),
        }