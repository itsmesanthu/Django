from django.urls import path
from .views import home,register,loginview,dashboard,logout_view,staff,manage_staff,add,edit_staff,del_staff
urlpatterns=[
    path('home/',home,name='home'),
    path('register/',register,name='register'),
    path('login/',loginview,name='login'),
    path('admin_dash/',dashboard,name='admin_dash'),
    path('logout/',logout_view,name='logout'),
    path('staff/',staff,name='staff'),
    path('manage/',manage_staff,name='manage'),
    path('add/',add,name='add_staff'),
    path('edit/<int:id>/',edit_staff,name='edit'),
    path('delete/<int:id>/',del_staff,name='delete')

]