from django.db import models

# Create your models here.
class Event(models.Model):
    production = models.CharField(max_length=100)
    thumb = models.ImageField(default='default.png', blank=True)
    performance_date = models.TextField(blank=True)
    location = models.TextField(blank=True)
    body = models.TextField()
    posting_date = models.DateTimeField(auto_now_add=True)
    #complete this database later
    #production to be a dropdown menu
    #slug based on production name won't work
    #date of production - calendar needed. Plus date of post. Two types of date.
