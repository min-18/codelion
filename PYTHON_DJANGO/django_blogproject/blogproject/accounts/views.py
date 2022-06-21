from django.shortcuts import redirect, render
# db에 저장된 회원인지 아닌지 여부를 판단해주는 내장된 기능
from django.contrib import auth

# models.py에 유저와 관련된 객체를 생성해주지 않았지만 쟝고는 내부에 user라고 하는 내장된 객체 가진다.
from django.contrib.auth.models import User

def login(request):
    # POST 요청이 들어오면 사용자가 입력한 로그인 처리.
    if request.method =="POST":
        userid = request.POST['username']
        userpwd = request.POST['password']
        # authenticate를 통해 사용자가 입력한 회원데이터와 db에 저장된 데이터를 대조해 맞으면 로그인, 아니면 none 반환.
        user = auth.authenticate(request, username=userid, password=userpwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'login.html')
            
    # GET 요청이 들어오면 login form을 담고 있는 login.html 띄워주는 역할.
    else:
        return render(request, 'login.html') 
