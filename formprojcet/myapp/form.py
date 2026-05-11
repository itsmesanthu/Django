from django import forms
class studentForm(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField()
    dob=forms.DateField()
    email=forms.EmailField()
    phno=forms.IntegerField()
    branch=forms.CharField()
