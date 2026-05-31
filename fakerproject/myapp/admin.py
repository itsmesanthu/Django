from django.contrib import admin
from .models import employee
class employeeAdmin(admin.ModelAdmin):
    list_display=['name','dob','job','place','email']
admin.site.register(employee)
