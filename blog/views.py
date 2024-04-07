from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, Comment
from .forms import CommentForm, BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django_summernote.widgets import SummernoteWidget


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
            comments = post.comments.filter(approved=True).order_by("-created_on")
            liked = post.likes.filter(id=request.user.id).exists()

            featured_image_url = None
            if post.featured_image:
                featured_image_url = post.featured_image.url

            context = {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "featured_image_url": featured_image_url,  
            }
            return render(request, "post_detail.html", context)
        except Post.DoesNotExist:
            return redirect('blog')

    def post(self, request, slug, *args, **kwargs):
        try:
            post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
            comments = post.comments.filter(approved=True).order_by("-created_on")
            liked = post.likes.filter(id=self.request.user.id).exists()
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment_form.instance.email = request.user.email
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
            else:
                comment_form = CommentForm()
            context = {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            }
            return render(request, "post_detail.html", context)
        except Post.DoesNotExist:
            return redirect('blog') 

class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def delete_post(request, id):

    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, f'Successfully deleted post "{post.title}".')

    context = {
        'messages': messages,
    }

    return redirect('blog')


@login_required
def add_post(request):
    if not request.user.is_superuser:
        messages.error(request, "Only store owners can access this.")
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            post = form.save(commit=False)
            post.status = 1

            if not post.featured_image:
                post.featured_image = 'media/noimage.jpg'  

            post.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect('blog')
        else:
            messages.error(request, 'Failed to add menu item.')
    else:
        form = BlogForm()

    template = 'add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_post(request, id):
  post = get_object_or_404(Post, id=id)
  if not request.user == post.author:
      messages.error(request, "You are not authorized to edit this post.")
      return redirect('blog')

  if request.method == 'POST':
      form = BlogForm(request.POST, request.FILES, instance=post)
      if form.is_valid():
          form.save()
          messages.success(request, 'Successfully edited blog post!')
          return redirect('blog')
      else:
          messages.error(request, 'Failed to edit blog post.')
  else:
      form = BlogForm(instance=post)

  template = 'add_post.html'  
  context = {
      'form': form,
  }
  return render(request, template, context)


@login_required
def delete_comment(request, post_slug, comment_id):
    post = get_object_or_404(Post, slug=post_slug)
    comment = get_object_or_404(Comment, post=post, id=comment_id)

    if comment.name == request.user.username:
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
        return redirect('post_detail', slug=post_slug)
    else:
        messages.error(request, 'You are not authorized to delete this comment.')
        return redirect('post_detail', slug=post_slug)