import datetime

from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    manufacturer = models.CharField(max_length=255)
    release_date = models.DateTimeField('release date')
    media_format = models.CharField(max_length=255)
    generation = models.SmallIntegerField()
    youtube_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    map_link = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Platforms"


class Developer(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    date_founded = models.DateTimeField('date established')
    num_employees = models.IntegerField()
    status = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    map_link = models.CharField(max_length=255)

    platforms = models.ManyToManyField(Platform)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Developers"


class Game(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    release_date = models.DateTimeField('release date')
    genre = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    ESRB_rating = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)

    developer = models.ForeignKey(Developer)
    platforms = models.ManyToManyField(Platform)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Games"
