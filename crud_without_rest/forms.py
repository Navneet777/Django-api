from django import forms
from crud_without_rest.models import Employee
class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal=self.cleaned_data['esal']
        if inputsal < 5000:
            raise forms.ValidationError('The minimum salary should be 5000')
        return inputsal
    class Meta:
         model=Employee
         fields='__all__'
