from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CustomUserCreationForm,TaskForm

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


def TaskCreate(request):
    if request.user.is_authenticated:
        form = TaskForm()
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                user_form = form.save(commit=False)
                user_form.user = request.user
                user_form.save()
                return redirect('/')
        data = {
            'form':form
        }
        return render(request,'tasks/task-create.html',data)
    else:
        messages.success(request,"Login First to create Tasks")
        return redirect('login')