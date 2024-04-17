from django.shortcuts import render, redirect
from .forms import Register
from django.contrib import messages
from django.contrib.auth import get_user_model
from . models import OtpToken
from . forms import Register
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "home.html")

def signup(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account is created, Please verify your email')
            return redirect('email_v', username=request.POST['username'])
    return render(request, 'signup.html', {'form':form})


def email_verify(request, username):
    user = get_user_model().objects.get(username=username)
    otp = OtpToken.objects.filter(user=user).last()
    
    if request.method == "POST":
        if otp.code == request.POST['otp_code']:
            if otp.exp_code_date > timezone.now():
                user.is_active = True
                user.save()
                messages.success(request, "Account verified successfully")
                return redirect("signin")
            else:
                messages.warning(request, "OTP has expired")
                return redirect("email_verification", username=user.username)
        else:
            messages.warning(request, "Invalid OTP")
            return redirect("email_verification")
    context = {}
    return render(request, "verify_token.html", context)            
            
    
    
def singin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:    
            login(request, user)
            messages.success(request, f"Hi {request.user.username}")
            return redirect("home")
        
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("signin")
        
    return render(request, "login.html")