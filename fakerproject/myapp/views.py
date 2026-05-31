from django.shortcuts import render
from myapp.models import employee
def employeeview(request):
    f=employee.objects.all()
    d={'fake':f}
    return render(request,'myapp/fake.html',d)