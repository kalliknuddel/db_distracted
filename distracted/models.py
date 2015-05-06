from django.db import models


# Create your models here.
class Series (models.Model):
    series_id = models.IntegerField()
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    overview = models.CharField(max_length=400)
    banner = models.URLField()
    first_aired = models.DateField("FirstAired")

    def __str__(self):
        return self.name

class Actor (models.Model):
    actor_id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Roles (models.Model):
    actor = models.ForeignKey(Actor)
    series = models.ForeignKey(Series)
    name = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    image = models.URLField()

    def __str__(self):
        return actor.name % " as " % name

