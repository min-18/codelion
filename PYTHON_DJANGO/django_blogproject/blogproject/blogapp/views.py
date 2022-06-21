# redirect ; 특정 url 로 다시 이동해라 
from django.shortcuts import render, redirect, get_object_or_404

# from blogproject.blogapp.forms import BlogForm
from .models import Blog
from django.utils import timezone

from .forms import BlogForm, BlogModelForm, CommentForm

# 홈페이지
def home(request):

    #  DB로부터 데이터를 가져와 render의 3번째 인자로 딕셔너리형태로 index.html에 업데이트

    # QuerySet : 데이터베이스로부터 전달받은 객체 목록
    # QuerySet 에 담긴 객체를 가져다 쓰려면 for문으로 

    # DB에 담긴 데이터 전부 가져오기
    posts = Blog.objects.all()
    # DB로부터 필터링해서 데이터 가져오기. 참고로 '-'는 역순으로 정렬
    # posts = Blog.objects.filter().order_by('-date')
    
    return render(request, 'index.html', {'posts':posts})

# 새 글을 작성하는 html 페이지
def new(request):
    return render(request, 'new.html')


# 블로그 글을 model에 저장하는 함수
def create(request):
    if (request.method == 'POST'):
        # Blog 객체 생성
        post = Blog()
        # 요청받은 내용대로 객체 안에 넣기
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        # 저장
        post.save()

    return redirect('home')
    
# django form 을 이용해서 데이터를 입력받는 함수 ; GET 요청과 POST 요청 둘다 처리가 가능하다.
# GET 요청 -> 사용자한테 정보를 입력받을 html 틀 갖다줘.
# POST 요청 -> get요청으로 받은 틀에 사용자가 입력한 데이터를 처리해줘.
def formcreate(request):
    # POST 요청
    # 참고로 'POST' 이렇게 대문자로 작성해야 먹힌다.
    if (request.method == 'POST'):
        # 입력 내용을 DB에 저장
        # 참고로 파일을 입력받고 싶으면 request.FILES
        form = BlogForm(request.POST)
        # 요청들어온 형태가 유효한지 체크
        if form.is_valid():
            # 유효하다면 저장
            # models.py에 있는 블로그 객체 생성하고 데이터를 하나씩 넣어줌.
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    # GET 요청
    else:
        # 입력받을 수 있는 html 틀 가져오기
        form = BlogForm()
    # django form으로 만든 BlogForm 객체 생성한 걸(form) 딕셔너리 형태로 form_create.html 에 넘겨줌.
    return render(request, 'form_create.html', {'form': form})


# model form으로 만들어진 form은 models.py에서 정의한 모델을 기반으로 만들어져 자체적으로 save 메서드를 갖고 있다.
# 반면 django form 으로 만들어진 form은 models.py에서 정의한 객체를 만들고 값을 넣어준 다음 그 객체에서 save해줘야함.
def modelformcreate(request):
    if (request.method == 'POST' or request.method == 'FILES'):
        form = BlogModelForm(request.POST, request.FIELS)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = BlogModelForm()
    
    # 'form_create.html' 그대로 사용해도 상관없음.
    return render(request, 'form_create.html', {'form': form})

# 상세페이지 보여지도록 하는 함수 ; 어떤 데이터를 넘겨줄지 정의하는 부분
# url path 정의할 때 blog_id 변수 가져옴.
def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 가져와서
    # Blog 객체를 가져올 건데 pk값이 blog_id인 객체를 가져올 거야. 
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    comment_form = CommentForm()
    # blog_id 번째 블로그 글을 detail.html 로 띄워주는 코드
    return render(request, 'detail.html', {'blog_detail': blog_detail, 'comment_form':comment_form})

# 사용자가 작성한 댓글을 저장하는 함수
def create_comment(request, blog_id):
    # POST형식으로 들어온 요청을 처리
    filled_form = CommentForm(request.POST)

    # 사용자가 작성한 댓글이 유효하다면 저장.
    if filled_form.is_valid():
        # 근데 주의. 저장하기 전에 어떤 글의 댓글인지 알기 위한 blog_id도 함께 저장해야함.
        # -> 아직 저장하지 않고 대기
        finished_form = filled_form.save(commit=False)
        # -> 어떤 글에 대한 댓글인지 CommentForm 의 post 정보 입력
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        # -> 그 다음 저장.
        finished_form.save()

    return redirect('detail', blog_id)
