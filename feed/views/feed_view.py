from django.views.generic import View
from django.shortcuts import render


class FeedView(View):
    template_name = "feed_view.html"

    def get(self, request):
        return render(request, self.template_name, {})
