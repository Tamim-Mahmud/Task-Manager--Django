from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm, AddTaskForm
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
def task_view(request,pk):
    if request.user.is_authenticated:
        individual_task=Tasks_list.objects.get(id=pk)
        return render(request, 'task_view.html',{'individual_task':individual_task})
    else:
        messages.success(request, "You need to login....")
        return redirect('home')
def delete_task(request,pk):
    if request.user.is_authenticated:
        delete_record= Tasks_list.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Task deleted Successfully....")
        return redirect('home')
    else:
       messages.success(request, "Please login....")
       return redirect('home')
def update_task(request,pk):
    if request.user.is_authenticated:
        instance = Tasks_list.objects.get(id=pk)
        form = AddTaskForm(request.POST or None, instance=instance)
        if request.method == 'POST' or None:
            if form.is_valid():
                form.save()
                messages.success(request,"Task Has been updated .....")
                return redirect('home')
        return render(request,'update_task.html',{'form':form})
    else:
        messages.success(request,'Please login first ....')
        return redirect('home')
    
def add_task(request):
    form =AddTaskForm(request.POST , request.FILES)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid():
                task=form.save(commit=False)
                task.user = request.user
                task.save()
                messages.success(request,"Task Saved")
                return redirect('home')
        return render(request,'add_task.html',{'form':form})
    else:
        messages.success(request,"Log in first......")
        return redirect('home')