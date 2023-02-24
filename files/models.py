from django.db import models

# Create your models here.

class NewUser(models.Model):
    fName = models.CharField(max_length=30)
    sName = models.CharField(max_length=30)
    tName = models.CharField(max_length=50)
    ctName = models.CharField(max_length=50)

    