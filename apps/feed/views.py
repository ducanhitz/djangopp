import django.contrib.auth.models
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from apps.feed.forms import NewPostForm

from apps.feed.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from apps.users.models import User

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'show_post.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-date_posted')
    

@login_required
def show_user_post(request):
    user = request.user
    user_posts_list = Post.objects.filter(
        user_name=user).order_by('-date_posted')
    return render(request, 'user_post.html', {
        'user_posts_list': user_posts_list,
    })


@login_required
def create_post(request):
    user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_name = user
            data.save()
            from pprint import pprint
            pprint(data)
            messages.success(request, f'Upload successfully!')
            return redirect('show_user_post')
    else:
        form = NewPostForm()
    return render(request, 'create_post.html', {
        'form': form
    })
