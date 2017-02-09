from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import UserForm


class AddUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = "add.html"

    def form_valid(self, form):
        user = form.save()
        user.save()
        return redirect(reverse("add_identity_view"))
