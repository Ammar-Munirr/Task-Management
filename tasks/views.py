from django.shortcuts import render,redirect
from django.views import generic
from .forms import CustomUserCreationForm

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
