from django.shortcuts import render
from myapp.models import Product
def prodcutview(request):
    p=Product.objects.all()
    d={'prod':p}
    return render(request,'product.html',d)