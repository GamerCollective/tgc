"""
A ``Collective`` is a group of ``TGCUser``s.
"""
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Collective(models.Model):
    name = models.CharField(max_length=140)
    members = models.ManyToManyField("tgcprofile.TGCUser", through="collective.Membership")
    description = models.TextField()
    tags = models.ManyToManyField("collective.Tag")
    date_created = models.DateField(editable=False, default=timezone.now)
    is_public = models.BooleanField(default=True)
