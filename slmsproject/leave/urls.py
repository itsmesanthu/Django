from django.urls import path
from .views import apply_leave,my_leaves,view_leaves
urlpatterns=[
    path('leave/',apply_leave,name="apply_leave"),
    path('myleave',my_leaves,name='my_leave'),
    path('view_leave',view_leaves,name='view_leave')
]