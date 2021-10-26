from django.contrib.auth.models import User
from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    achievements = models.ManyToManyField(Achievement)
    friends = models.ManyToManyField(User, related_name='friends')
    friend_requests = models.ManyToManyField(User, related_name='requests_sent_to')
    position_lon = models.FloatField()
    position_lat = models.FloatField()
    points = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.get_full_name()


class Steps(models.Model):
    how_many = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User)


class Goal(models.Model):
    position_lon = models.FloatField()
    position_lat = models.FloatField()
    sponsor = models.CharField(null=True, blank=True, max_length=255)
