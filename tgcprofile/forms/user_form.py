from django.contrib.auth.models import User
from django.forms import ModelForm, Form, CharField, PasswordInput


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput)

    class Meta:
        model = User
        fields = ["email", "username", "password"]
