from django import forms


class InviteMemberForm(forms.Form):
    email = forms.EmailField()
    collective = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(InviteMemberForm, self).__init__(*args, **kwargs)
        self.fields['collective'].choices = [(c.pk, c.name) for c in user.collective_set.all()]
