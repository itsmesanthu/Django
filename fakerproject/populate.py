import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakerproject.settings')
django.setup()
from myapp.models import employee
from faker import Faker
f=Faker('en-In')
def populate(n):
    for i in range(n):
        fname=f.name()
        fdob=f.date_of_birth()
        fjob=f.job()
        fplace=f.address()
        femail=f.email()
        s=employee.objects.get_or_create(name=fname,dob=fdob,job=fdob,place=fplace,email=femail)
populate(20)
