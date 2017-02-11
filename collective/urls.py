from __future__ import unicode_literals

from django.conf.urls import url
import views

app_name = 'collective'
collective_url_patterns = [
    url(r'^collective/add/$', views.AddCollectiveView.as_view(template_name="add.html"), name="add_collective_view"),
]
