from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from identity.models import Identity


class DashboardView(LoginRequiredMixin, ListView):
    model = Identity
    login_url = "/account/login/"
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context
