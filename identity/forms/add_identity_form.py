from django.forms import ModelForm
from identity.models import Identity


class AddIdentityForm(ModelForm):
    class Meta:
        model = Identity
        exclude = ['user']
