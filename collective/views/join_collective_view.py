from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.shortcuts import redirect
from django.views.generic import View

from common import messages
from ..services import add_tgcuser_to_collective, get_collective_by_pk


class JoinCollectiveView(LoginRequiredMixin, View):
    def get(self, request, collective_pk):
        if request.user.is_authenticated():
            collective = get_collective_by_pk(collective_pk)
            try:
                add_tgcuser_to_collective(request.user, collective)
            except IntegrityError:
                messages.info(request, "You are already a member of {}".format(collective.name))
                return redirect(reverse("dashboard_view"))
            messages.success(request, "You joined {}".format(collective.name))
            return redirect(reverse("dashboard_view"))
