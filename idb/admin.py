from django.contrib import admin

# Register your models here.
from idb.Models import Game, Platform, Developer

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Developer)
