from xml.dom import ValidationErr
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import re
from .validators import password_validate
from django.core.exceptions import ValidationError

def home(request):
	return render(request, "home.html")

def signup(request):
	try:
		if request.method == "POST":	
			if User.objects.filter(username=request.POST["username"]).exists():
				return render(request, "signup_done.html",{'message':'해당 아이디와 일치한 회원이 존재합니다. 다시 시도해주세요'})
			password_validate(request.POST["password1"])
			if request.POST["password1"] == request.POST["password2"]:
				user = User.objects.create_user(
					request.POST["username"], password = request.POST['password1'])
			auth.login(request, user)
			return redirect("home")
		return render(request,"signup.html")
	except ValidationError:
		return render(request, "signup_done.html",{'message':'비밀번호 형식에 맞지 않습니다.'})



def login(request):
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호를 확인해주세요'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    return render(request, 'login.html') 
