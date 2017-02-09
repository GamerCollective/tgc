from django.forms import ModelForm
from identities.models import Identity


class AddIdentityForm(ModelForm):
    class Meta:
        model = Identity
        exclude = ['user']
