from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Competitions(models.Model):
    name = models.CharField(max_length=100)
    days_counter = models.IntegerField()
    rounds_per_day = models.IntegerField()
    gates_per_round = models.IntegerField()
    location = models.CharField(max_length=200)
    userID = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.name, self.location)