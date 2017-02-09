from django.forms import Form, CharField, PasswordInput


class LoginForm(Form):
    username = CharField(max_length=35)
    password = CharField(widget=PasswordInput)
