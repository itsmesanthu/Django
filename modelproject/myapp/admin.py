from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'gender', 'dob', 'place', 'email']

admin.site.register(Student, StudentAdmin)