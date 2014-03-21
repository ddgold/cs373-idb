from django.contrib import admin

# Register your models here.
from idb.Models import Game, Platform, Developer

class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Game, GameAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Developer, DeveloperAdmin)

