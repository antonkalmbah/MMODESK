from django.forms import ModelForm
from .models import Comment, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'name', 'description', 'image', 'content']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']