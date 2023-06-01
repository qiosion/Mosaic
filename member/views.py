from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# 회원가입
def signup(request):
    if request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            member = signupForm.save(commit=False)
            member.save()
            return redirect('index') # 회원가입 성공 시 메인으로 돌아감
    else:
        signupForm = UserCreationForm()
        context = {'signupForm': signupForm}
        return render(
            request,
            'member/signup.html',
            context
        )

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
    return redirect('/')