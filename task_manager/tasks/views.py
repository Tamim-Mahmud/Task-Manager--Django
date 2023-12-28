from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout

from .forms import SignUpForm
from django.contrib import messages
from rest_framework import  viewsets
from .serializer import TaskSerializer
from .models import Tasks_list

# Create your views here.
class TaskApiView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Tasks_list.objects.all()
    

def home(request):
    tasks_list =Tasks_list.objects.all()
    print(tasks_list[1].title)
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
        return render(request, 'home.html',{'tasks_list':tasks_list})
def logout_user(request):
    logout(request)
    return redirect('home')
def reg_user(request):
    if request.method == "POST":
        form= SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user =authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, "You have successfully registered....")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})
    