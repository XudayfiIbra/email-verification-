from django.shortcuts import render, redirect
from .forms import Register
from django.contrib import messages


def signup(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account is created, Please verify your email')
            return redirect('email_v', username=request.POST['username'])
    return render(request, 'signup.html', {'form':form})


def email_verify(request):
    pass