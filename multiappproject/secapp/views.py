from django.http import HttpResponse
# Create your views here.
def viwe1(request):
    a="<h1>this is response from 2st app"
    return HttpResponse(a)