from django.db import models
# Each user should have an email, name, and mobile number.

class UserData(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.TextField()