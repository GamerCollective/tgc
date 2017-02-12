from __future__ import unicode_literals

from django import forms

from ..models import Membership


class AcceptInviteForm(forms.ModelForm):
    class Meta:
        model = Membership
        exclude = ["date_joined"]
        widgets = {'member': forms.HiddenInput(), "collective": forms.HiddenInput()}
