from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout

def index(request):
    context = {
        'page_title':'Home',
    }
    return render(request, 'index.html', context)

def LoginView(request):
    context = {
        'page_title':'Login',
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    
    return render(request, 'login.html', context)

def LogoutView(request):
    context = {
        'page_title':'Logout',
    }

    if request.method == 'POST':
        if request.POST['logout'] == 'Submit':
            logout(request)
            
        return redirect('index')
    
    return render(request, 'logout.html', context)