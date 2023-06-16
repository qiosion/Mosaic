from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# 회원가입
def signup(request):
    if request.method == "GET":
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

            # email_validator = EmailValidator()
            # try:
            #     email_validator(email)
            # except ValidationError:
            #     error_message = "유효한 이메일 주소를 입력해주세요."
            #     context = {'error_message': error_message}
            #     return render(request, 'member/signup.html', context)

            user = User(first_name=first_name, username=username)
            user.set_password(password) # 비밀번호 암호화
            user.email = email
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
        return render(
            request,
            'member/login.html',
        )
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                error_message = "아이디 또는 비밀번호가 일치하지 않습니다"
                return render(request,
                              'member/login.html',
                              {'error_message': error_message})
        else:
            error_message = "아이디 또는 비밀번호를 입력해주세요"
            return render(request,
                          'member/login.html',
                          {'error_message': error_message})
    return HttpResponse("Invalid request")

# 로그아웃
def logout(request):
    auth_logout(request)
    # return redirect('/forum/list')
    return redirect('index')

def delete(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        return redirect('index')
    return render(request, '')

def update(request):
    if request.method == "POST":
        user = request.user

        new_pw = request.POST.get('password')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        new_em = f"{email1}@{email2}"

        user.email = new_em
        user.set_password(new_pw)
        user.save()
        return redirect('mypage')
    elif request.method == "GET":
        user = request.user
        return render(request, 'member/Mypage.html', {'user': user})