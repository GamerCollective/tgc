from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.shortcuts import redirect

from ..forms import AddCollectiveForm
from ..models import Collective
from ..services import add_tgcuser_to_collective


class AddCollectiveView(LoginRequiredMixin, CreateView):
    model = Collective
    login_url = "/account/login/"
    form_class = AddCollectiveForm
    template_name = "add_collective.html"

    def form_valid(self, form):
        collective = form.save()
        add_tgcuser_to_collective(self.request.user, collective)
        return redirect(reverse("dashboard_view"))
