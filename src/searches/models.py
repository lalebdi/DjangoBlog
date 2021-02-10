from django.conf import settings
from django.db import models

# Create your models here.


class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)