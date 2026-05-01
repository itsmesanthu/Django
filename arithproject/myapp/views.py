from django.http import HttpResponse
def lowercase(request):
    s=input("enter the strinh")
    n=""
    for i in range(0,len(s)):
        if "A"<= s[i]<="Z":
            n=n+chr(ord(s[i])+32)
        else:
            n=n+s[i]
    return HttpResponse(n)