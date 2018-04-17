from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
   """A db object representing comments made on a timetable. """
   message = models.TextField()
   owner = models.ForeignKey(User)
   last_updated = models.DateTimeField(auto_now=True)