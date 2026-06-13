from django.shortcuts import render,redirect,get_object_or_404
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
            return redirect('staff')
        return HttpResponse("Username and password invalid")
    return render(request, 'login.html')
@login_required
def dashboard(request):
    if request.user.profile.role!='admin':
        return render(request,'staff_dashboard.html')
    return render(request,'admin_dashboard.html')
def logout_view(request):
    logout(request)
    return redirect('home')
@login_required
def staff(request):
   return render(request,'staff_dashboard.html')

@login_required
def manage_staff(request):
    if request.user.profile.role!='admin':
        return redirect('staff_dashboard')
    staff_list=User.objects.filter(profile__role='staff')
    return render(request,'manage_staff.html',{'staff_list':staff_list})
@login_required
def add(request):
    if request.user.profile.role!='admin':
        return redirect('staff')
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(
            username=username,
            password=password
        )
        Profile.objects.create(
            user=user,
            role='staff'
        )
        return redirect('manage')
    return render(request,'add_staff.html')
@login_required
def edit_staff(request,id):
    if request.user.profile.role!='admin':
        return redirect('staff')
    user=get_object_or_404(User,id=id)
    if request.method=='POST':
        user.username=request.POST['username']
        user.save()
        return redirect('manage')
    return render(request,'Edit_staff.html',{'user': user})
@login_required
def del_staff(request,id):
    if request.user.profile.role!='admin':
        return redirect('staff')
    user=get_object_or_404(User,id=id)
    user.delete()
    return redirect('manage')