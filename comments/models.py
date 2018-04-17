from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
   """A db object representing comments made on a timetable. """
   message = models.TextField()
   owner = models.ForeignKey(Student)
   last_updated = models.DateTimeField(auto_now=True)