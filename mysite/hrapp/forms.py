from django import forms
from hrapp.models import Employee, Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = 'first_name','last_name','middle_name','DOB','join_date'