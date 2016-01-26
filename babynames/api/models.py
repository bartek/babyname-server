from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

from .constants import GENDER_CHOICES, NEUTRAL


class Name(models.Model):
    name = models.CharField(max_length=45)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES)

    def __unicode__(self):
        return self.name


class NameCollection(models.Model):
    """
    Encompasses the link between a unique code and lists of names.

    A user can have a collection of names under a specific `share_code`. The
    names include both favourites and ignored names. This model is effectively
    the persistent state container for the client-side application.
    """

    share_code = models.CharField(max_length=10, primary_key=True)
    preferred_gender = models.CharField(max_length=8, choices=GENDER_CHOICES, default=NEUTRAL)
    favourites = ArrayField(models.IntegerField(), default=list)
    ignored = ArrayField(models.IntegerField(), default=list)

    def __unicode__(self):
        return '{0} (Gender: {1})'.format(self.share_code, self.preferred_gender)
