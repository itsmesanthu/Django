from django.shortcuts import render
from myapp.forms import studentform
def formview(request):
    s=studentform()
    if request.method=="POST":
        s=studentform(request.POST)
        if s.is_valid():
            name = s.cleaned_data['name']
            age = s.cleaned_data['age']
            place = s.cleaned_data['place']
            email = s.cleaned_data['email']

            d={'name':name,'age':age,'place':place,'email':email}
            return render(request,'output.html',d)

    d={'form':s}
    return render(request,'forms.html',d)