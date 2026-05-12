from django import forms
class studentform(forms.Form):
    name =forms.CharField()
    age=forms.IntegerField()
    place=forms.CharField()
    email=forms.EmailField()
    def clean_name(self):
        n=self.cleaned_data['name']
        if len(n)<=3:
            raise forms.ValidationError("min nounber of chass must be greter than 3")
        return n
