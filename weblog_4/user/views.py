from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLogin,UserRegister
from django.contrib import messages
# Create your views here.

def user_login(request):   
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate (request,username =username,password = password )
            if user is not None:
                login (request ,user
                )
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('blog:all_articles')
            else:
                messages.error(request,'user or pass in not correct','warning')

    else:
        form = UserLogin()
    return render (request,'user/login.html',{'form':form})



def user_signup(request):
	if request.method == 'POST':
		form = UserRegister(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			User.objects.create_user(data['username'], data['email'], data['password1'])
			messages.success(request, 'you registered successfully, now log in', 'success')
			return redirect('user:login')
	else:
		form = UserRegister()
	return render(request, 'user/signup.html', {'form':form})


def user_logout(request):
	logout(request)
	messages.success(request, 'you logged out successfully', 'success')
	return redirect('blog:all_articles')