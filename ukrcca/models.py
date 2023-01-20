from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Competitions(models.Model):
    name = models.CharField(max_length=100)
    days_counter = models.IntegerField()
    rounds_per_day = models.IntegerField()
    gates_per_round = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.name, self.location)

class Score(models.Model):
    driver = models.ForeignKey(User, on_delete=models.PROTECT)
    round = models.IntegerField()
    comp_id = models.ForeignKey(Competitions, on_delete=models.CASCADE)
    penalties = ArrayField(
        models.CharField(max_length=300, blank=True),
        size=None,
        )
    total_points = models.IntegerField(blank=True)
    time_completed = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.penalties

class TruckClass(models.Model):
    name = models.CharField(max_length=10)

class Truck(models.Model):
    name = models.CharField(max_length=20)
    truck_type = models.ManyToManyField(TruckClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name