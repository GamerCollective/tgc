"""
Members of a ``Collective`` can tag their collective to indicate what types of games they generally play
(FPS, MMO, RTS etc) or what types of members it has (Casual, Competitive, Speed runners, etc).
"""
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25)
