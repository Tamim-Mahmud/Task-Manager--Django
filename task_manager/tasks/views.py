from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
# from .forms import SignUpForm, AddRecordForm
# from .models import Record
# for lgin log out message
from django.contrib import messages

# Create your views here.

def home(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"You Have Loged In Successfully .....")
            return redirect('home')
        else:
            messages.error(request,"Error Occured . Please Try again .....")
            return redirect('home')
    else:
        return render(request, 'home.html',{})
def logout_user(request):
    logout(request)
    return redirect('home')