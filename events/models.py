from django.db import models

# Create your models here.
class Event(models.Model):
    production = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #complete this database later
    #production to be a dropdown menu
    #slug based on production name won't work
    #date of production - calendar needed. Plus date of post. Two types of date.
