from django.contrib import admin
from .models import Blog, Comment

# 쟝고는 db에 담긴 데이터를 admin 사이트에서 관리할 수 있다.

admin.site.register(Blog)
admin.site.register(Comment)
