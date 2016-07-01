from django.conf.urls import url
import views


app_name = 'tgcprofile'
tgcprofile_url_patterns = [
    url(r"^account/add/$", views.AddUserView.as_view(), name='add_user_view'),
    url(r"^account/login/$", views.LoginView.as_view(), name='login_view'),
    url(r"^account/logout/$", views.LogoutView.as_view(), name='logout_view'),
    url(r"^account/edit/$", views.EditUserView.as_view(), name='edit_user_view'),
]
