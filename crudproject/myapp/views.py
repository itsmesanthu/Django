from django.shortcuts import render,redirect
from .models import employee
from .form import employeeform

def display(request):
    e=employee.objects.all()
    d={'emp':e}
    return render(request,'myapp/display.html',d)
def insert(request):
    f=employeeform()
    if request.method=="POST":
        f=employeeform(request.POST)
        if f.is_valid():
            f.save(commit=True)
            return redirect('/')
    d={'form':f}
    return render(request,'myapp/insert.html',d)   
def update(request,id):
    f=employee.objects.get(id=id)
    if request.method=='POST':
        e=employeeform(request.POST,instance=f)
        if e.is_valid():
            e.save(commit=True)
            return redirect('/')
    e=employeeform(instance=f)
    d={'form':e}
    return render(request,'myapp/insert.html',d)    
def delete(request,id):
    e=employee.objects.get(id=id)
    e.delete()
    return redirect('/')