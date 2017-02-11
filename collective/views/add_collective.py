from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.shortcuts import redirect

from ..forms import AddCollectiveForm
from ..models import Collective


class AddCollectiveView(LoginRequiredMixin, CreateView):
    model = Collective
    login_url = "/account/login/"
    form_class = AddCollectiveForm
    template_name = "add.html"

    def form_valid(self, form):
        return redirect(reverse("dashboard_view"))
