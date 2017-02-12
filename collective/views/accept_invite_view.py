from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import View

from ..forms import AcceptInviteForm
from tgcprofile.services import get_tgcuser_by_email
from ..services import (validate_token, add_tgcuser_to_collective, get_collective_by_pk, get_payload_from_token,
                        invalidate_invite_token)


class AcceptInviteView(View):
    def get(self, request):
        payload = get_payload_from_token(request.GET.get("token"))
        if request.user.is_authenticated():
            collective = get_collective_by_pk(payload.collective_pk)
            form = AcceptInviteForm(initial={"collective": collective, "member": request.user})
            return render(request, "accept.html", {"collective": collective, "form": form})
        elif get_tgcuser_by_email(payload.email):
            messages.info(request, "Please log in to accept invitation")
            return redirect(reverse("login_view") + "?next={}?token={}".format(request.path, request.GET.get("token")))
        else:
            messages.info(request, "Please sign up ")
            return redirect(reverse("add_user_view") + "?next={}?token={}".format(request.path, request.GET.get("token")))

    def post(self, request):
        collective = get_collective_by_pk(request.POST.get("collective"))
        if request.user.is_active:
            if validate_token(request.user.email, request.GET.get("token")):
                message = "You joined {}".format(collective.name)
                try:
                    add_tgcuser_to_collective(request.user, collective)
                except IntegrityError:
                    message = "You are already a member of {}".format(collective.name)
                invalidate_invite_token(request.user.email)
                messages.success(request, message)
                return redirect(reverse("dashboard_view"))
            messages.error(self.request, "Invalid token")
        return redirect(reverse("home_view"))
