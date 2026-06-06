from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        User.objects.create_user(username=username,email=email,password=password)
        return redirect('login')
    return render(request,'register.html')
def loginview(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("username and password invalid..:)")
    return render(request,'login.html')
@login_required
def dashboard(request):
    return render(request,'dashboard.html')
def logoutview(requset):
    logout(requset)
    return redirect('login')