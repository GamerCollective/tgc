from __future__ import unicode_literals

from django.conf.urls import include, url
import views

app_name = 'collective'
collective_url_patterns = [
    url(r"collective/", include([
        url(r'^add/$', views.AddCollectiveView.as_view(), name="add_collective_view"),
        url(r'^invite/$', views.InviteMembersView.as_view(), name="invite_members_view"),
        url(r"^accept/$", views.AcceptInviteView.as_view(), name="accept_invite_view"),
        url(r"^view/$", views.UserCollectiveView.as_view(), name="user_collective_view"),
        url(r"^view/(?P<collective_pk>\d+)/$", views.CollectiveView.as_view(), name="collective_view"),
        url(r"^search/$", views.SearchCollectivesView.as_view(), name="search_collectives_view"),
    ]))
]
