from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView, ListView
from django.shortcuts import render, redirect

from .forms import AddIdentityForm
from .models import Identity


class AddIdentityView(LoginRequiredMixin, CreateView):
    model = Identity
    login_url = "/account/login/"
    form_class = AddIdentityForm
    template_name = "add.html"

    def form_valid(self, form):
        form.instace.user = self.request.user
        form.save()
        return redirect(reverse("dashboard_view"))


class DeleteIdentityView(LoginRequiredMixin, DeleteView):
    model = Identity
    login_url = "/account/login/"

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class DashboardView(LoginRequiredMixin, ListView):
    model = Identity
    login_url = "/account/login/"
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context
