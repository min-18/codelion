

from django.conf import settings
from django.contrib import admin
from django.urls import path
from blogapp import views
# 위의 blogapp과 views가 겹치기 때문에 as로 새로운 이름 명명해줘도 되고
# include로 각각의 앱에서 계층적으로 url을 관리해줘도 된다. ; 근데 이게 더 좋다!
from accounts import views as accounts_views

# 아래 두줄은 미디어 파일에 접근하는 url 추가하기 위해 가져와야함. 관례적으로 쓰기 때문에 그냥 외우자.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # html form 을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form 을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    # django modelform 을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # 블로그글의 상세페이지로 이동하는 path
    # 객체를 만들면 자동으로 생성되는 primary key를 이용하여 상세페이지마다 구분되는 url 생성
    # 예시. http://127.0.0.1:8000/detail/1 (primary key부분)
    # 상세페이지를 구분짓는 url을 위해 pk값도 함께 detail 함수에 넘겨줘야함.
    # <int:blog_id> ; blog_key라는 변수로 views.py 파일의 detail 함수에 넘겨준다는 의미
    path('detail/<int:blog_id>', views.detail, name='detail'),
    
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),

    path('login/', accounts_views.login, name='login'),


] 

# 미디어 파일에 접근할 수 있는 url도 추가해줘야함.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)