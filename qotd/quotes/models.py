from django.db import models

class Quote(models.Model):
    category = models.CharField(max_length=100)
    published_date = models.DateTimeField("date published")
    content = models.CharField(max_length=500)
