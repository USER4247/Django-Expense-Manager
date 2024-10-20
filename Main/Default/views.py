from django.shortcuts import render , HttpResponse , redirect

def home(req):
    return render(req , 'Pages/Home.html',{})

def redirectToSignIn(req):
    return redirect('manageUsers/loginUser')

def redirectToSignUp(req):
    return redirect('manageUsers/signup')

def redirectToShowDetails(req):
    return redirect('manageUsers/user_list')

def redirectToDashboard(req):
    return redirect('manageExpense/userDashboard') 