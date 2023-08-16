from django.urls import path
from .views import  (
    ArtikelListView,
    ArtikelDetailView,
    ArtikelKategoriListView,
    ArtikelCreateView,
    ArtikelManageView,
    ArtikelDeleteView,
    ArtikelUpdateView,
)

app_name = 'artikel'
urlpatterns = [
    path('manage/update/<slug:pk>', ArtikelUpdateView.as_view(), name='update'),
    path('manage/delete/<slug:pk>', ArtikelDeleteView.as_view(), name='delete'),
    path('manage/', ArtikelManageView.as_view(), name='manage'),
    path('create/', ArtikelCreateView.as_view(), name='create'),
    path('detail/<slug:slug>', ArtikelDetailView.as_view(), name='detail'),
    path('kategori/<slug:kategori>/<slug:page>', ArtikelKategoriListView.as_view(), name='category'),
    path('<slug:page>', ArtikelListView.as_view(), name='list'),
]