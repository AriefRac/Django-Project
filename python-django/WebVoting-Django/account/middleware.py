from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages


class AccountCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulname = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == '1':
                if modulname == 'voting.views':
                    error = True
                    if request.path == reverse('fetch_ballot'):
                        pass
                    else:
                        messages.error(request, "Tidak memilliki akses")
                        return redirect(reverse('adminDashboard'))
            elif user.user_type == '2':
                if modulname == 'administrator.views':
                    messages.error(request, "Tidak memiliki hak akses")
                    return redirect(reverse('voterDashboard'))
        else:
            if request.path == reverse('account_login') or request.path == reverse('account_register') or modulname == 'django.contrib.auth.views' or request.path == reverse('account_login'):
                pass
            elif modulname == 'administrator.views' or modulname == 'voting.views':
                messages.error(request, "Perlu login terlebih dahulu")
                return redirect(reverse('account_login'))
            else:
                return redirect(reverse('account_login'))
