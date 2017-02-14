from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

from collective.services import get_collective_by_pk


class CollectiveView(View):
    def get(self, request, collective_pk):
        collective = get_collective_by_pk(collective_pk)
        return render(request, "collective_view.html", {"collective": collective})
