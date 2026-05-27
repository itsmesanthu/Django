from myapp.models import student
from django import forms
class studentview(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'