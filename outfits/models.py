from django.db import models
from sources.models import Source

class Outfit(models.Model):
    outfit_id = models.CharField(max_length=50)
    source_id = models.ForeignKey(Source)
    description = models.TextField()
