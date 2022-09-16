from sqlite3 import Timestamp
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class tweet(models.Model):
    content = models.CharField(max_length=256)
    Timestamp = models.DateTimeField(auto_now_add=True)