from django.shortcuts import render
from myapp.models import employdata
def employview(request):
    e=employdata.objects.all()
    d={'employ':e}
    return render(request,'employ.html',d)