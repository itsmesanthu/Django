from django.shortcuts import render,redirect
from .models import student
from .form import studentform
def display(request):
    e=student.objects.all()
    d={'dis':e}
    return render(request,'display.html',d)
def insert(request):
    f=studentform()
    if request.method=="POST":
        f=studentform(request.POST, request.FILES)
        if f.is_valid():
            f.save(commit=True)
            return redirect('/')
    d={'form':f}
    return render(request,'insert.html',d)
def update(request,id):
    e=student.objects.get(id=id)
    if request.method=="POST":
        f=studentform(request.POST,instance=e)
        if f.is_valid():
            f.save(commit=True)
            return redirect('/')
    f=studentform(instance=e)
    d={'form':f}
    return render(request,'insert.html',d)
def delete(request,id):
    f=student.objects.get(id=id)
    f.delete()
    return redirect('/')