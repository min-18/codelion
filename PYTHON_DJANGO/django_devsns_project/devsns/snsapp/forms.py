from django import forms
from .models import *


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['comment']


class FreePostform(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'body']


class FreeCommentform(forms.ModelForm):
    class Meta:
        model = FreeComment
        # fields = '__all__'
        fields = ['comment']