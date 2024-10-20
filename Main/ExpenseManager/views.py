from django.shortcuts import render , HttpResponse , redirect ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
@login_required(login_url='/manageUsers/loginUser')
def userDashboard(req):
    return render(req , 'Pages/ExpensesDashboard.html',{}) 

def logOut(req):
    logout(req)
    response = HttpResponseRedirect('/manageUsers/loginUser')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # HTTP 1.1.
    response['Pragma'] = 'no-cache'  # HTTP 1.0.
    response['Expires'] = '0'  # Proxies.
    return response