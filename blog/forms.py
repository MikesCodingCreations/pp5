from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]

class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['author', 'created']