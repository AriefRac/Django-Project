from django.contrib import admin
from django.urls import path
from .views import index, LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
