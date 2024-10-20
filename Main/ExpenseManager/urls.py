from django.urls import path 
from .import views

urlpatterns = [
    path("userDashboard",views.userDashboard,name="userDashboard"),
    path("logOut",views.logOut,name='logOut')
]