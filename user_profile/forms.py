from  django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('full_name', 'email', 'contact', 'emp_code','rpa', 'java', 'cplusplus', 'csharp', 'selenium'
                  , 'python', 'powerbi', 'azuredevops')
        labels = {'full_name': 'Full_Name',
                  'email': 'Email',
                  'contact': 'Contact',
                  'emp_code': 'Emp_Code',
                  'rpa': 'RPA',
                  'java': 'Java',
                  'cplusplus': 'C++',
                  'csharp': 'C#',
                  'selenium': 'Selenium',
                  'python': 'Python',
                  'powerbi': 'PowerBI',
                  'azuredevops': 'AzureDevOps'
                  }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['rpa'].empty_label = "select"
        self.fields['java'].empty_label = "select"
        self.fields['python'].empty_label = "select"
        self.fields['powerbi'].empty_label = "select"
        self.fields['csharp'].empty_label = "select"
        self.fields['cplusplus'].empty_label = "select"
        self.fields['selenium'].empty_label = "select"
        self.fields['azuredevops'].empty_label = "select"
        self.fields['emp_code'].required = False
