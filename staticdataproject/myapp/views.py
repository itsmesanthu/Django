from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Product
import json
class ProductDetail(View):
    def get(self,request,*args, **kwargs):
        prod=Product.objects.get(id=2)
        prod_data={
            'name':prod.name,
            'price':prod.price,
            'quantity':prod.quantity,
            'descripation':prod.description,
            'brand':prod.brand
        }
        json_data=json.dumps(prod_data)
        return HttpResponse(json_data,content_type='application/json')