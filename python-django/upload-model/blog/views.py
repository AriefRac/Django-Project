from django.shortcuts import render, HttpResponseRedirect
from .forms import PostForm
from .models import PostModel


def index(request):
    posts = PostModel.objects.all()
    context = {
        'page_title': 'List Post',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def create(request):
    post_form = PostForm(request.POST or None)

    if request.method == 'POST':

        if post_form.is_valid():
            PostModel.objects.create(
                judul=post_form.cleaned_data.get('judul'),
                body=post_form.cleaned_data.get('body'),
                category=post_form.cleaned_data.get('category'),
            )
            return HttpResponseRedirect("/blog")

    context = {
        'page_title': 'create post',
        'post_form': post_form,
    }

    return render(request, 'blog/create.html', context)
