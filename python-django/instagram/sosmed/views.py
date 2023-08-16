from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Instagram
from .forms import InstagramForm

# Create your views here.

def index(request):
    semua_akun = Instagram.objects.all()
    forms = InstagramForm(request.POST or None)

    # untuk update

    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return redirect(reverse('sosmed:index'))

    context = {
        'page_title':'List Akun',
        'semua_akun': semua_akun,
        'forms':forms,
    }

    return render(request, 'sosmed/index.html', context)

def create(request):
    forms = InstagramForm(request.POST or None)

    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return redirect(reverse('sosmed:index'))

    context = {
        'page_title':'Buat Akun',
        'forms':forms,
    }

    return render(request, 'sosmed/create.html', context)

def delete(request, delete_id):
    Instagram.objects.filter(id=delete_id).delete()
    return redirect(reverse('sosmed:index'))

def update(request, update_id):
    semua_akun = Instagram.objects.all()
    akun_update = Instagram.objects.get(id=update_id)

    data = {
        'nama_depan': akun_update.nama_depan,
        'nama_belakang': akun_update.nama_belakang,
        'username': akun_update.username,
    }

    forms = InstagramForm(request.POST or None, initial=data, instance=akun_update)

    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return redirect(reverse('sosmed:index'))

    context = {
        'page_title':'Update Akun',
        'forms':forms,
        'semua_akun':semua_akun,
    }

    return render(request, 'sosmed/index.html', context)