import datetime

from django.db import models


class Platform(models.Model):
    '''
    Platform Model that represents a video game platform

    @type name: models.CharField(255)
    @cvar name: Name of the platform
    @type manufacturer: models.CharField(255)
    @cvar manufacturer: the manufacturer of the platform
    @type release_date: models.DateField()
    @cvar release_date: date the platform was released
    @type media_format: models.Charfield(255)
    @cvar media_format: the form(s) of media (CDs, cartridge, etc) used by platform
    @type generation: models.SmallIntegerField()
    @cvar generation: the console generation of the platform
    @type youtube_link: models.CharField(255)
    @cvar youtube_link: link to a youtube video
    @type image_link1: models.CharField(255)
    @cvar image_link1: link to an image
    @type image_link2: models.CharField(255)
    @cvar image_link2: link to an image
    @type image_link3: models.CharField(255)
    @cvar image_link3: link to an image
    '''
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
    

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Platforms"


class Developer(models.Model):
    '''
    Developer Model that represents a video game developer

    @type name: models.CharField(255)
    @cvar name: Name of the developer
    @type date_founded: models.DateField()
    @cvar date_founded: date the developer studio was founded
    @type num_employees: models.SmallIntegerField()
    @cvar num_employees: the number of employees currently working at the studio
    @type status: models.CharField(255)
    @cvar status: the current state of the studio, active or defunct
    @type address: models.CharField(255)
    @cvar address: the address of the developer's HQ
    @type map_link: models.CharField(511)
    @cvar map_link: link to the Google Map of the address
    @type image_link1: models.CharField(255)
    @cvar image_link1: link to an image
    @type image_link2: models.CharField(255)
    @cvar image_link2: link to an image
    @type image_link3: models.CharField(255)
    @cvar image_link3: link to an image
    @type platforms: models.ManyToManyField('Platform')
    @cvar platforms: The platforms this studio developers for
    '''
    name = models.CharField(max_length=255)
    date_founded = models.DateField('date established')
    num_employees = models.IntegerField()
    status = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    map_link = models.CharField(max_length=511)
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
    '''
    Game Model that represents a video game

    @type title: models.CharField(255)
    @cvar title: Title of the game
    @type release_date: models.DateField()
    @cvar release_date: date the game was released
    @type genre: models.CharField(255)
    @cvar genre: genre of the game
    @type publisher: models.CharField(255)
    @cvar publisher: the publisher firm that released this game
    @type ESRB_rating: models.CharField(255)
    @cvar ESRB_rating: the offical ESRB rating
    @type youtube_link: models.CharField(255)
    @cvar youtube_link: link to a youtube video
    @type image_link1: models.CharField(255)
    @cvar image_link1: link to an image
    @type image_link2: models.CharField(255)
    @cvar image_link2: link to an image
    @type image_link3: models.CharField(255)
    @cvar image_link3: link to an image
    '''
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
