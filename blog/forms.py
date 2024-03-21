from django import forms
from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget()) 
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['author', 'created', 'likes', 'status', 'slug']
