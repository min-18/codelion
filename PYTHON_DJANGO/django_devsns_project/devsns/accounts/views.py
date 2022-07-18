from django.shortcuts import redirect, render

# 로그인 기능 위해
from django.contrib import auth
# 회원가입 위해 User 객체 필요
from django.contrib.auth.models import User

def login(request):
    # POST 면 로그인 요청
    if request.method == "POST":
        userid = request.POST['username']
        userpwd = request.POST['password']

        user = auth.authenticate(request, username=userid, password=userpwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            return render(request, 'bad_login.html')

    # GET 이면 로그인하는 html 띄우기.
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['repeat']

        if password1 == password2:
            # 회원가입 ; 새로운 user 객체 생성
            new_user = User.objects.create_user(
                username = username, password=password1
            )
            # 로그인
            auth.login(request, new_user)
            # 홈으로 리다이렉션
            return redirect('home')
    else:
        return render(request, 'register.html')