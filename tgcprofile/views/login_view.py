from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import View

from ..forms import LoginForm


class LoginView(View):
    template_name = "tgcprofile/login.html"

    @staticmethod
    def get(request):
        form = LoginForm()
        return render(request, "login.html", context={"form": form})

    @staticmethod
    def post(request):
        username, password = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("dashboard_view"))
        return redirect(reverse("login_view"))
