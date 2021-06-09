from django.db import models

# Create your models here.
class Resource(models.Model):
    links_and_text = models.TextField()
    docs = models.FileField()
