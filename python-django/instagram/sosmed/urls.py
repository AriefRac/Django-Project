from django.urls import path
from . import views

app_name = 'sosmed'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<slug:delete_id>', views.delete, name='delete'),
    path('update/<slug:update_id>', views.update, name='update'),
]