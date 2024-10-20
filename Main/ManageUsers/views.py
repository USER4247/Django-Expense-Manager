from django.shortcuts import render , HttpResponse , redirect
from .models import UserData # model to store user data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
def addUsers(req):
    return HttpResponse("IMPLEMENT ADD USERS")

def loginUser(req):
    if req.method == 'POST':
        
        email = req.POST['email']
        password = req.POST['password']
        user = authenticate(req, username=email, password=password)
        print("INSIDE IF " , user)
        if user is not None:
            login(req, user)
            print('LOGIN SUCCEESS')
            return redirect('userDashboard')
        else:
            messages.error(req, 'Invalid email or password')
    return render(req , 'Auth/LogIn.html',{})

def signup(req):
    if req.method == 'POST':
        email = req.POST['email'] # probably should add regex check here 
        password = req.POST['password']
        name = req.POST['name']
        phone = req.POST['phone'] # probably should add regex check here 
        print(email,password,name,phone)
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")
        # <1> add user -----------------------------------------------------------------
        user = User.objects.create_user( username=email ,first_name=name, email=email, password=password)
        user.save()
        # <2> add user data to model ---------------------------------------------------
        user_data = UserData(name=name, phone=phone, email=email)
        user_data.save()
        return redirect('LogIn')
    return render(req , 'Auth/SignUp.html',{}) 

def user_list(request):
    user_data_list = UserData.objects.all()
    paginator = Paginator(user_data_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'UserData/UserData.html', {'page_obj': page_obj})