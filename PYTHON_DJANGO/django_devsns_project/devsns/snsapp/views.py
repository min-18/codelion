from django.shortcuts import redirect, render,get_object_or_404

from .forms import *
from .models import *
# Create your views here.

def home(request):
    # 홈에 글들의 목록을 띄워주기 위해 글 객체들 불러오기
    # posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')

    return render(request, 'index.html', {'posts':posts})

    # 공통부분은 base.html 에 담아 상속받아 재사용하기

# 쟝고는 한 url 안에 post와 get 모두 처리가능.
def postcreate(request):
    # post 요청이면 입력값 저장
    if request.method == "POST" or request.method == 'FILES':
        # POST요청 들어온 거 폼에 다 담고
        form = Postform(request.POST, request.FILES)

        # form 유효성 검사
        if form.is_valid():
            # 모델form은 save()매서드가 있어서 바로 저장.
            form.save()
            return redirect('home')
        
    
    # get 요청이면 입력 html 띄우기
    else:
        form = Postform()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    # post = Post.objects.filter(pk=post_id)
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = Commentform()

    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

# 댓글저장
def new_comment(request, post_id):
    # POST요청 받은 거 담고
    filled_form = Commentform(request.POST)
    # 유효한지 검사하고
    if filled_form.is_valid():
        # 바로 저장하면 안되고 
        # 꼭 넣어줘야하는 정보인데 아직 넣지 않은 정보; 어떤 게시물의 댓글인지에 대한 FK정보도 넣어주기.
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
        # detail페이지인데 내가 댓글 단 페이지(post_id)도 같이 명시
        return redirect('detail', post_id)


def freehome(request):
    # 홈에 글들의 목록을 띄워주기 위해 글 객체들 불러오기
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')

    return render(request, 'free_index.html', {'freeposts':freeposts})

# 쟝고는 한 url 안에 post와 get 모두 처리가능.
def freepostcreate(request):
    # post 요청이면 입력값 저장
    if request.method == "POST" or request.method == 'FILES':
        # POST요청 들어온 거 폼에 다 담고
        form = FreePostform(request.POST, request.FILES)

        # form 유효성 검사
        if form.is_valid():
            # 모델form은 save()매서드가 있어서 바로 저장.
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('freehome')
        
    # get 요청이면 입력 html 띄우기
    else:
        form = FreePostform()
    return render(request, 'free_post_form.html', {'form':form})

def freedetail(request, post_id):
    # post = Post.objects.filter(pk=post_id)
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentform()

    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

# 댓글저장
def new_freecomment(request, post_id):
    # POST요청 받은 거 담고
    filled_form = FreeCommentform(request.POST)
    # 유효한지 검사하고
    if filled_form.is_valid():
        # 바로 저장하면 안되고 
        # 꼭 넣어줘야하는 정보인데 아직 넣지 않은 정보; 어떤 게시물의 댓글인지에 대한 FK정보도 넣어주기.
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
        # detail페이지인데 내가 댓글 단 페이지(post_id)도 같이 명시
        return redirect('freedetail', post_id)
