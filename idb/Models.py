import datetime

from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    release_date = models.DateField('release date')
    media_format = models.CharField(max_length=255)
    generation = models.SmallIntegerField()
    youtube_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    image_link1 = models.CharField(max_length=255)
    image_link2 = models.CharField(max_length=255)
    image_link3 = models.CharField(max_length=255)
    map_link = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Platforms"


class Developer(models.Model):
    name = models.CharField(max_length=255)
    date_founded = models.DateField('date established')
    num_employees = models.IntegerField()
    status = models.CharField(max_length=255)
    map_link = models.CharField(max_length=255)
    image_link1 = models.CharField(max_length=255)
    image_link2 = models.CharField(max_length=255)
    image_link3 = models.CharField(max_length=255)
    
    platforms = models.ManyToManyField(Platform)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Developers"


class Game(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField('release date')
    genre = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    ESRB_rating = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)
    image_link1 = models.CharField(max_length=255)
    image_link2 = models.CharField(max_length=255)
    image_link3 = models.CharField(max_length=255)
    
    developer = models.ForeignKey(Developer)
    platforms = models.ManyToManyField(Platform)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Games"
