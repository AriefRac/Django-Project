from django.shortcuts import render


def index(request):
    context = {
        'judul': 'Home',
        'heading': 'Home Page',
    }

    return render(request, 'index.html', context)
