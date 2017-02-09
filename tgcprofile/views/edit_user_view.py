from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import UpdateView


class EditUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "edit.html"
    login_url = "/account/login/"
    fields = ['username', 'email']

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return redirect(reverse("dashboard_view"))
