from django.shortcuts import render
from .form import studentview
from django.http import HttpResponse
def formview(request):
    f=studentview()
    if request.method=="POST":
        f=studentview(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("your record has been submitted")
    d={'form':f}
    return render(request,'myapp/form.html',d)