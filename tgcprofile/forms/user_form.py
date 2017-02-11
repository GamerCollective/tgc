from __future__ import unicode_literals

from django.forms import ModelForm, CharField, PasswordInput

from ..models import TGCUser


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput)

    class Meta:
        model = TGCUser
        fields = ["email", "username", "password"]
