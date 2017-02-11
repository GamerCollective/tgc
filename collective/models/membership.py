"""
Intermediate model for managing memberships.
"""
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Membership(models.Model):
    member = models.ForeignKey("tgcprofile.TGCUser")
    collective = models.ForeignKey("collective.Collective")
    date_joined = models.DateField(editable=False, default=timezone.now)
