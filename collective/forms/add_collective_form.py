from __future__ import unicode_literals

from django import forms
from ..models import Collective, Tag


def get_tags():
    return [(tag.pk, tag.name) for tag in Tag.objects.all()]


class AddCollectiveForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(choices=get_tags)

    class Meta:
        model = Collective
        exclude = ["members"]
