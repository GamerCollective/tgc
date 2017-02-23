from __future__ import unicode_literals

from django.conf.urls import include, url
import views

app_name = 'feed'
feed_url_patterns = [
    url(r"feed/", include([
        url(r'^$', views.FeedView.as_view(), name="feed_view"),
    ]))
]
