from django.urls import path 
from .import views

urlpatterns = [
    path("addUser",views.addUsers,name="addUser"),
    path("loginUser",views.loginUser , name='LogIn'),
    path("signup",views.signup , name='signup'),
    path("user_list",views.user_list,name='user_list')
]