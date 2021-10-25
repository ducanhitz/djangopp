from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from apps.feed.forms import NewPostForm
from apps.feed.models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from pprint import pprint
# Create your views here.


@login_required
def show_post(request):
    user = request.user
    posts_list = Post.objects.filter(user_name=user)
    return render(request, 'show_post.html', {
        'posts_list': posts_list,
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
            messages.success(request, f'Posted Successfully')
            return redirect('show_post')
        else:
            pprint('form is not valid')
    else:
        form = NewPostForm()
    return render(request, 'create_post.html', {'form': form})
