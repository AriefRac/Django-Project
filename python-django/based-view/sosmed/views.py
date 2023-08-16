from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView, RedirectView, View

from .models import Instagram
from .forms import InstagramForm

# Create your views here.

class InstagramIndexView(TemplateView):
    template_name = 'sosmed/index.html'

    def get_context_data(self, *args,**kwargs):
        semua_akun = Instagram.objects.all()
        context = {
        'page_title':'List Akun Instagram',
        'semua_akun': semua_akun,
        }
        return context

class SosmedDeleteView(RedirectView):
    pattern_name = 'sosmed:list'

    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs['delete_id']
        Instagram.objects.filter(id=delete_id).delete()
        return super().get_redirect_url()
    
class SosmedFormView(View):
    template_name = 'sosmed/create.html'
    form = InstagramForm()
    mode = None
    context = {}

    def get(self,*args,**kwargs):
        if self.mode == 'update':
            akun_update = Instagram.objects.get(id=kwargs['update_id'])
            data = akun_update.__dict__
            self.form = InstagramForm(initial=data, instance=akun_update)
            
        self.context = {
            'page_title':'Buat Akun',
            'forms':self.form,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwarg):
        self.form = InstagramForm(self.request.POST)
        if self.form.is_valid():
            self.form.save()

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