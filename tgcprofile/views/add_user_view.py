from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import UserForm
from ..models import TGCUser


class AddUserView(CreateView):
    model = TGCUser
    form_class = UserForm
    template_name = "add.html"

    def form_valid(self, form):
        user = form.save()
        user.save()
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user:
            login(self.request, user)
        if self.request.GET.get("next"):
            return redirect(self.request.GET.get("next"))
        return redirect(reverse("add_identity_view"))
