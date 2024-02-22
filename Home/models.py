from django.db import models

class Report(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    location = models.CharField(max_length = 75,null=True, blank=True)
    dateandtime = models.CharField(max_length = 30, null=True, blank=True)
    heading = models.CharField(max_length = 30, null=True, blank=True ) 
    description = models.TextField()

