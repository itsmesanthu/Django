from django.urls import path
from .views import home,register,loginview,dashboard,logout_view
urlpatterns=[
    path('home/',home,name='home'),
    path('register/',register,name='register'),
    path('login/',loginview,name='login'),
    path('admin_dash/',dashboard,name='admin_dash'),
    path('logout/',logout_view,name='logout')

]