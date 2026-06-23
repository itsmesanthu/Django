from django.views.generic import View
from myapp.models import Product
import json
from django.http import HttpResponse
from django.core.serializers import serialize

class ProductDetails(View):
    def get(self, request, *args, **kwargs):
        prod = Product.objects.all()
        json_data = serialize('json', [prod])
        return HttpResponse(json_data,content_type='application/json')