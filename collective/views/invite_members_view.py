from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.shortcuts import redirect

from ..forms import InviteMemberForm
from ..services import send_invitation_email, get_invite_link, get_collective_by_pk


class InviteMembersView(LoginRequiredMixin, FormView):
    login_url = "/account/login/"
    form_class = InviteMemberForm
    template_name = "invite.html"

    def get_form_kwargs(self):
        kwargs = super(InviteMembersView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        email, collective_pk = form.cleaned_data["email"], form.cleaned_data["collective"]
        link = get_invite_link(email, int(collective_pk), self.request.user.pk)
        send_invitation_email(email, link)
        return redirect(reverse("dashboard_view"))


