from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView

from identities.models import Identity


class DeleteIdentityView(LoginRequiredMixin, DeleteView):
    model = Identity
    login_url = "/account/login/"

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
