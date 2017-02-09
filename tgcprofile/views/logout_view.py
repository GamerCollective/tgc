from __future__ import unicode_literals

from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect(reverse("login_view"))
