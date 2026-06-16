from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Leave
@login_required
def apply_leave(request):
    if request.method=='POST':
        leave_type = request.POST.get('leave_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('End_date')
        reason = request.POST.get('reason')
        if not (leave_type and start_date and end_date and reason):
            context = {
                'error': 'All fields are required.',
                'leave_type': leave_type,
                'start_date': start_date,
                'End_date': end_date,
                'reason': reason,
            }
            return render(request, 'apply_leave.html', context)
        Leave.objects.create(
            user=request.user,
            leave_type=leave_type,
            start_date=start_date,
            End_date=end_date,
            reason=reason,
            status='Pending',
        )
        return redirect('staff')
    return render(request,'apply_leave.html')
@login_required
def my_leaves(request):
    leaves=Leave.objects.filter(user=request.user)
    return render(request,'my_leaves.html',{'leaves':leaves})

@login_required
def view_leaves(request):
    if request.user.profile.role!='admin':
        return redirect('staff_dashboard')
    leaves=Leave.objects.all()
    return render(request,'views_leave.html',{'leaves':leaves})