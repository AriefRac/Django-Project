from django.shortcuts import render


def index(request):
    context = {
        'judul': 'Home',
        'desc': 'Page Home',
    }
    return render(request, 'index.html', context)
