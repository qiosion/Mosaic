from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


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
        email = request.POST.get('email')
        # email1 = request.POST.get('email1')
        # email2 = request.POST.get('email2')
        if first_name and username and password and email:
            user = User(first_name=first_name, username=username, email=email)
            user.set_password(password)  # 비밀번호 암호화
            user.save()

            return redirect('index')
        if User.objects.filter(username=username).exists():
            error_message = "이미 사용 중인 아이디 입니다."
            context = {'error_message': error_message}
            return render(request, 'member/signup.html', context)
        else:
            success_message = "사용 가능한 아이디입니다"
            context = {'success_message': success_message}
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
    return redirect('index')

def delete(request):
    if request.method == "POST":
        password = request.POST.get('password')
        user = authenticate(request, username=request.user, password=password)

        if user is not None:
            user.delete()
            logout(request)
            return redirect('index')
        else:
            error_message = "비밀번호가 일치하지 않습니다"
            return render(request,
                          'member/delete.html',
                          {'error_message': error_message})

    elif request.method == 'GET':
        return render(request,
                      'member/delete.html')

@login_required(login_url='/member/login')
def update(request):
    if request.method == "POST":
        user = request.user
        print('post에서 user : ', user)

        new_pw = request.POST.get('password')
        new_email = request.POST.get('email')
        if new_pw and new_email:
            user.email = new_email
            user.set_password(new_pw)
            user.save()

            update_session_auth_hash(request, user)

            return redirect('mypage')
        else:
            error_message = "폼을 입력해주세요"
            return render(request,
                          'member/Mypage.html',
                          {'error_message': error_message})
    elif request.method == "GET":
        user = request.user
        print('get에서 user : ', user)
        return render(request,
                      'member/Mypage.html',
                      {'user': user})