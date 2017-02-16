from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..services import get_memberships_for_tgcuser


class UserCollectiveView(LoginRequiredMixin, ListView):
    template_name = "user_collective_view.html"
    login_url = "account/login"

    def get_queryset(self):
        return get_memberships_for_tgcuser(self.request.user)
