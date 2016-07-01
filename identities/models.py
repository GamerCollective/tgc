from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Identity(models.Model):
    user = models.ForeignKey(User)
    game = models.CharField(max_length=35)
    username = models.CharField(max_length=35)
