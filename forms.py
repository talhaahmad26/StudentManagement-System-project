from django import forms 
from .models import student

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['student_id','first_name','last_name','email','field_of_study','gpa']
        labels ={
            'student_id': 'Student  ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email ',
            'field_of_study': 'Field of Study',
            'gpa': 'GPA',
        }
        widgets = {
            'student_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }

