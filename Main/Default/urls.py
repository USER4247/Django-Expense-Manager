from django.urls import path 
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path("redirectToSignIn",views.redirectToSignIn,name='redirectToSignIn'),
    path("redirectToSignUp",views.redirectToSignUp,name='redirectToSignUp'),
    path("redirectToShowDetails",views.redirectToShowDetails,name='redirectToShowDetails'),
    path("redirectToDashboard",views.redirectToDashboard,name='redirectToDashboard')
]