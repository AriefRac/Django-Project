from django.urls import path
from .views import *

app_name = 'sosmed'
urlpatterns = [
    path('delete/<slug:delete_id>', SosmedDeleteView.as_view(), name='delete'),
    path('update/<slug:update_id>', SosmedFormView.as_view(mode='update'), name='update'),
    path('create/', SosmedFormView.as_view(), name='create'),
    path('', InstagramIndexView.as_view(), name='index'),
]