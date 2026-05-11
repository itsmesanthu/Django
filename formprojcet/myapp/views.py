from django.shortcuts import render
from myapp.form import studentForm
from django.http import HttpResponse
def formview(request):
    f=studentForm()
    if request.method=="POST":
        f=studentForm(request.POST)
        if f.is_valid():
            return HttpResponse("your record has been submitted")
    d={'form':f}
    return render(request,'form.html',d)    
