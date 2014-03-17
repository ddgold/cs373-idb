import datetime

from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    release_date = models.DateTimeField('release date')
    publisher = models.CharField(max_length=255)
    ESRB_rating = models.CharField(max_length=255)

    developer = models.ForeignKey(Developer)
    platforms = models.ManyToManyField(Platform)

    def __unicode__(self):
	return self.title

    class Meta:
	ordering = ['title']
	verbose_name_plural = "Games"


class Developer(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    date_founded = models.DateTimeField('date established')
    num_employees = models.IntegerField()
    status = models.CharField(max_length=255)

    platforms = models.ManyToManyField(Platform)

    class Meta:
	ordering = ['name']
	verbose_name_plural = "Developers"


class Platform(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    release_date = models.DateTimeField('release date')
    generation = models.SmallIntegerField()
    media_format = models.CharField(max_length=255)

    class Meta:
	ordering = ['name']
	verbose_name_plural = "Platforms"
