from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.shortcuts import redirect

from identity.forms import AddIdentityForm
from identity.models import Identity


class AddIdentityView(LoginRequiredMixin, CreateView):
    model = Identity
    login_url = "/account/login/"
    form_class = AddIdentityForm
    template_name = "add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect(reverse("dashboard_view"))
