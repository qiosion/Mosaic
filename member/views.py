from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# 회원가입
def signup(request):
    if request.method == "GET":
        # signupForm = SignupForm()
        # context = {'signupForm': signupForm}
        return render(
            request,
            'member/signup.html',
        )
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        if first_name and username and password and email1 and email2:
            email = f"{email1}@{email2}"
            user = User(first_name=first_name, username=username, password=password, email=email)
            user.save()
            return redirect('index')  # 회원가입 성공 시 메인으로 돌아감
        else:
            error_message = "폼이 유효하지 않습니다"
            context = {'error_message': error_message}
            return render(request, 'member/signup.html', context)
    return HttpResponse("Invalid request")  # POST 메서드 외에는 처리하지 않음

# 로그인
def login(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        context = { 'loginForm': loginForm }
        return render(
            request,
            'member/login.html',
            context
        )
    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
        # return redirect('/forum/list')
        return redirect('login')

# 로그아웃
def logout(request):
    auth_logout(request)
    # return redirect('/forum/list')
    return redirect('index')