from django.conf.urls import url
import views

app_name = 'identities'
identity_url_patterns = [
    url(r"^dashboard/$", views.DashboardView.as_view(), name="dashboard_view"),
    url(r'^identity/add/$', views.AddIdentityView.as_view(template_name="add.html"), name='add_identity_view'),
    url(r'^identity/delete/$', views.DeleteIdentityView.as_view(), name='delete_identity_view')
]
