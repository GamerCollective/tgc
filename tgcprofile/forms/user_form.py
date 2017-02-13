from __future__ import unicode_literals

from django.forms import ModelForm, CharField, PasswordInput

from ..models import TGCUser


class UserForm(ModelForm):
    class Meta:
        model = TGCUser
        fields = ["email", "username", "password"]
        widgets = {"password": PasswordInput}

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
