from django.db import models

class Report(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    subject = models.CharField(max_length = 75)
    description = models.TextField()

