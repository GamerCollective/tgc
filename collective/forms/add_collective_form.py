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

    def __init__(self, *args, **kwargs):
        super(AddCollectiveForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({"id": "name", "class": "form-control"})
        self.fields['description'].widget.attrs.update({"id": "description", "class": "form-control", "rows": 3})
        self.fields['tags'].widget.attrs.update({"id": "tags", "class": "form-control"})
        self.fields['is_public'].widget.attrs.update({"id": "is_active"})
