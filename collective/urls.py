from __future__ import unicode_literals

from django.conf.urls import url
import views

app_name = 'collective'
collective_url_patterns = [
    url(r'^collective/add/$', views.AddCollectiveView.as_view(template_name="add.html"), name="add_collective_view"),
    url(
        r'^collective/invite/$',
        views.InviteMembersView.as_view(template_name="invite.html"),
        name="invite_members_view"
    ),
    url(r"^collective/accept/", views.AcceptInviteView.as_view(), name="accept_invite_view")
]
