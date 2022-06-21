from importlib.metadata import files
from xml.etree.ElementTree import Comment
from django import forms
# modelform으로 할 때
from .models import Blog, Comment

# 일반적인 form
class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    # 많은 문자열 받기 위해
    body = forms.CharField(widget=forms.Textarea)

# 모델을 기반으로 한 model form
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # Blog 객체의 모든 틀을 가져다 쓸거면 -> fields = '__all__' / 아니면 리스트형태로 필요한 것들만
        # fields = ['title', 'body']
        fields = '__all__'

# 댓글관련 model form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 데이터 모델짠 부분중에서 사용자한테 입력받을 부분.
        fields = ['comment']
        