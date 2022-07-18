from turtle import title
from django.db import models

from django.contrib.auth.models import User

# 익명게시판
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # 객체 추가될 때마다 그 당시의 시간대 자동저장
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ORM : 클래스를 이용해 db에 맵핑하는 모델
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment

# 자유게시판
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # 객체 추가될 때마다 그 당시의 시간대 자동저장
    date = models.DateTimeField(auto_now_add=True)
    # 작성자 => 장고에 내장된 User 객체를 참조해야.
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    

class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment