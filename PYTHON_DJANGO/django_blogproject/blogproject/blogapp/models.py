from tkinter import CASCADE
from django.db import models


# Blog 틀로 테이블의 뼈대를 구성한다고 생각.
# 나중에 사용자 입력을 받을 form 을 만들 때, 특히 model form을 쓰면 클래스의 요소들을 바로 가져다 쓸 수 있다. 

# 모델 요소를 추가해주고 나면 makemigrations 랑 migrate 해줘야한다.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # blogproject 안 media 폴더 내에 blog_photo라는 이름으로 된 폴더 생성되어 그 안에 사진들 담긴다.
    photo = models.ImageField(blank=True, null = True, upload_to = 'blog_photo')
    # auto_now_add=True -> 자동으로 현재 시간 추가해줌.
    date = models.DateTimeField(auto_now_add=True)

    # admin 사이트에서 제목이 바로 보이도록
    def __str__(self):
        return self.title


# 어떤 게시글에 달린 댓글인지 구분해주기 위해 Blog 클래스 참조해야 ; 다른 테이블에서 참조한, 연결된 키(Foreign key)
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    # Blog 객체를 참조하는 foreign key로 만들어짐. 
    # 만약 Blog 객체가 삭제되면 그 객체에 종속된 Comment도 같이 삭제된다는 의미.
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    # admin 사이트에서 댓글이 바로 보이도록
    def __str__(self):
        return self.comment
