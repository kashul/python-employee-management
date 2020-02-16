from django import forms
from .models import Employee


class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EmployeeForms, self).__init__(*args, **kwargs)
        self.fields['company'].empty_label = "select"
