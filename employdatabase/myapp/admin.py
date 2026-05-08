from django.contrib import admin
from .models import employdata
class employadmin(admin.ModelAdmin):
    list_display=['id','fname','lname','age','gender','dob','place','email']
admin.site.register(employdata,employadmin)