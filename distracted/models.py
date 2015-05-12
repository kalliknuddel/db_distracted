from django.db import models


# Create your models here.
class Series (models.Model):
    RUNNING = 'running'
    DISCONTINUED = 'discontinued'
    
    StatusTypes = (
                   (RUNNING, "Running"),
                   (DISCONTINUED, "Discontinued"),
                   )
    
    series_id   = models.IntegerField()
    name        = models.CharField (max_length=100)
    overview    = models.CharField (max_length=400)
    banner      = models.URLField ()
    first_aired = models.DateField ("FirstAired")
    network     = models.CharField (max_length=50, default='')
    rating      = models.CharField (max_length=10, default='0.0')
    voters      = models.IntegerField (default=0)
    runtime     = models.IntegerField (default=0)
    lastUpdate  = models.IntegerField (default=0)
    status      = models.CharField (max_length=15, choices=StatusTypes, default='running')

    def __str__ (self):
        return self.name

class Season (models.Model):
    season_id = models.IntegerField (primary_key=True)
    series_id = models.ForeignKey (Series)
    seasonNumber = models.IntegerField (unique=True)


class Episode (models.Model):
    id          = models.IntegerField (primary_key=True)
    director    = models.CharField (max_length=100)
    episodeName = models.CharField (max_length=100)
    firstAired  = models.DateField ("FirstAired")
    rating      = models.CharField (max_length=100)
    voters      = models.CharField (max_length=100)
    episodeNumber = models.IntegerField ()
    season_id    = models.ForeignKey (Season)
    series_id    = models.ForeignKey (Series)
    
    def __str__ (self):
        #    get Series Object
        series = Series.objects.get (series_id = self.series_id)
        season = Season.objects.get (season_id = self.season_id)
        return series.name + ": Season " + season.seasonNumber + " Episode " + self.episodeNumber + ": " + self.episodeName

class Actor (models.Model):
    actor_id = models.IntegerField ()
    name = models.CharField (max_length=50)

    def __str__ (self):
        return self.name


class Roles (models.Model):
    actor = models.ForeignKey (Actor)
    series = models.ForeignKey (Series)
    name = models.CharField (max_length=50)
    sort_order = models.IntegerField ()
    image = models.URLField ()

    def __str__ (self):
        return actor.name % " as " % name

