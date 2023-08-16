from django.shortcuts import render, redirect, reverse
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {
        'page_title': 'Post',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def create(request):
    data_form = PostForm(request.POST or None)
    if request.method == 'POST':
        if data_form.is_valid():
            data_form.save()
            return redirect(reverse('blog:index'))

    context = {
        'page_title': 'Create',
        'form': data_form,
    }
    return render(request, 'blog/create.html', context)
