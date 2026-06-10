from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth  import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role=role)
        return redirect('login')
    return render(request, 'register.html')
def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.profile.role == 'admin':
                return redirect('admin_dash')
            return HttpResponse("staff")
        return HttpResponse("Username and password invalid")
    return render(request, 'login.html')
@login_required
def dashboard(request):
    if request.user.profile.role!='admin':
        return HttpResponse("staff_dashboard")
    return render(request,'admin_dashboard.html')
def logout_view(request):
    logout(request)
    return redirect('home')