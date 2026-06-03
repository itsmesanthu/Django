from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from .models import student
class student_list(ListView):
    model=student
class student_details(DetailView):
    model = student
    template_name = 'myapp/student_details.html'
class student_update(UpdateView):
    model=student
    fields='__all__'
class student_delet(DeleteView):
    model=student
    success_url=reverse_lazy('student')