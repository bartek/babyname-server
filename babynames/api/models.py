from __future__ import unicode_literals

from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=45)
    gender = models.CharField(max_length=8, choices=(
        ('neutral', 'Gender Neutral'),
        ('boy', 'Boy'),
        ('girl', 'Girl'),
    ))
