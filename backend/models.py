from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.URLField(max_length=2000)
    short_url = models.CharField(max_length=30)
    created_on = models.DateTimeField()
    count = models.BigIntegerField(default=0)
