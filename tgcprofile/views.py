from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, View, UpdateView

from .forms import UserForm, LoginForm


class AddUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = "add.html"

    def form_valid(self, form):
        user = form.save()
        user.save()
        return redirect(reverse("add_identity_view"))


class EditUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "edit.html"
    login_url = "/account/login/"
    fields = ['username', 'email']

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return redirect(reverse("dashboard_view"))


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


class LogoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect(reverse("login_view"))
