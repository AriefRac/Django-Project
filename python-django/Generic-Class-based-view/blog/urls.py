from django.urls import path
from .views import (
    ArtikelDetailView,
    ArtikelFormView,
    ArtikelListView,
    ArtikelCreateView1,
    ArtikelCreateView2,
    ArtikelUpdateView1,
    ArtikelUpdateView2,
    ArtikelDeleteView,
    )
from .models import Artikel
from .forms import ArtikelForm



app_name = 'blog'
urlpatterns = [
    path('delete/<slug:pk>', ArtikelDeleteView.as_view(), name='delete'),
    path('update2/<slug:pk>', ArtikelUpdateView2.as_view(), name='update2'),
    path('update1/<slug:pk>', ArtikelUpdateView1.as_view(), name='update1'),
    path('create/', ArtikelCreateView2.as_view(), name='create'),
    # path('create/', ArtikelCreateView1.as_view(), name='create'),
    # path('create/', ArtikelFormView.as_view(), name='create'),
    # path('create/', FormView.as_view(form_class=ArtikelForm, template_name='blog/create.html'), name='create'),
    path('detail/<slug:slug>', ArtikelDetailView.as_view(model=Artikel), name='detail'),
    # path('detail/<slug:slug>', DetailView.as_view(model=Artikel), name='detail'),
    path('<slug:penulis>/<slug:page>', ArtikelListView.as_view(), name='list'),
    path('<slug:penulis>/', ArtikelListView.as_view(), name='list'),
    # path('', ArtikelListView.as_view(), name='list'),
]