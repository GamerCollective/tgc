from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from ..forms import SearchCollectivesForm
from ..services import get_active_collectives, get_collectives_by_tag_pks


class SearchCollectivesView(LoginRequiredMixin, View):
    template_name = "search_collectives_view.html"
    login_url = "account/login"

    def get(self, request):
        context = {
            "form": SearchCollectivesForm(),
            "collectives": get_active_collectives()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
            "form": SearchCollectivesForm(),
            "collectives": get_collectives_by_tag_pks(request.POST.getlist("tags"))
        }
        return render(request, self.template_name, context)
