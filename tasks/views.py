from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomUserCreationForm,TaskForm,TaskForm2
from .models import Tasks
from django.db.models import Q

def SignupView(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    data = {
        'form':form
    }
    return render(request,'registration/signup.html',data)

def home(request):
    if not request.user.is_authenticated:
        return render(request,'tasks/home.html')
    else:
        return redirect('/task-list')

def TaskCreate(request):
    if request.user.is_authenticated:
        form = TaskForm()
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                user_form = form.save(commit=False)
                user_form.user = request.user
                user_form.save()
                messages.success(request,'Task Added !')
                return redirect('task-list')
        data = {
            'form':form
        }
        return render(request,'tasks/task-create.html',data)
    else:
        messages.success(request,"Login First to create Tasks")
        return redirect('login')
    

def TaskUpdate(request,pk):
    if request.user.is_authenticated:
        try:
            task = Tasks.objects.filter(user=request.user).get(id=pk)
        except:
            messages.success(request,'The Task Not Found !')
            return redirect('task-list')
        form = TaskForm2(instance=task)
        if request.method=='POST':
            form = TaskForm2(request.POST,instance=task)
            if form.is_valid():
                form.save()
                messages.success(request,'Task Updated Successfully')
                return redirect('task-list')
        data = {
            'form':form
        }
        return render(request,'tasks/task-detail.html',data)
    else:
        messages.success(request,'Login First to Update the Task')
        return redirect('login')
    

def TaskList(request):
    if request.user.is_authenticated:
        if 'q' in request.GET:
            q = request.GET['q']
            multiple_q = Q(Q(user=request.user) & (Q(title__icontains=q) | Q(description__icontains=q)))
            tasks = Tasks.objects.filter(multiple_q)
        else:
            tasks = Tasks.objects.filter(user=request.user)
        data = {
            'tasks':tasks
        }
        return render(request,'tasks/task-list.html',data)
    else:
        messages.success(request,'Login First to Check the Tasks')
        return redirect('login')
    

def DeleteTask(request,pk):
    if request.user.is_authenticated:
        task = Tasks.objects.filter(user=request.user).get(id=pk)
        task.delete()
        messages.success(request,'Task Deleted Successfully !')
        return redirect('task-list')
    else:
        messages.success(request,'Must Login to delete task')
        return redirect('login')