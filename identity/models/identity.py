from __future__ import unicode_literals

from django.db import models


class Identity(models.Model):
    user = models.ForeignKey("tgcprofile.TGCUser")
    game = models.CharField(max_length=35)
    username = models.CharField(max_length=35)
