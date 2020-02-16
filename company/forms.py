from django import forms
from .models import Company


class CompanyForms(forms.ModelForm):

    class Meta:
        model = Company
        fields = "__all__"
