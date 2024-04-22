from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login,logout
# Create your views here.


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('user_register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('user_register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use")
            return redirect('user_register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "You have successfully registered. You can now log in.")
        return redirect('user_login')
    else:
        return render(request, 'user_register.html')
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('landing_page') 
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'user_login.html')

def user_logout(request):
    logout(request)
    # messages.success(request, "You have been logged out.")
    return redirect('landing_page')


