from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

from ..forms import SearchCollectivesForm
from ..services import get_active_collectives, get_collectives_by_tag_pks


class SearchCollectivesView(View):
    template_name = "search_collectives_view.html"

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
