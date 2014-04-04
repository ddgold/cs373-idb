from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from idb.models import Platform, Developer, Game

class PlatformResource(ModelResource):
    class Meta:
        queryset = Platform.objects.all()
        resource_name = 'platform'
        authentication = ApiKeyAuthentication()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'name': ['exact', 'starstwith', 'endswith', 'contains'],
            'manufacturer': ['exact', 'starstwith', 'endswith', 'contains'],
            'release_date': ['exact', 'lt', 'gt', 'lte', 'gte', 'range'],
            'media_format': ['exact', 'starstwith', 'endswith', 'contains'],
            'generation': ['exact', 'gt', 'gte', 'lt', 'lte', 'range'],
        }


class DeveloperResource(ModelResource):
    platforms = fields.ToManyField(PlatformResource, 'platforms')
    class Meta:
        queryset = Developer.objects.all()
        resource_name = 'developer'
        authentication = ApiKeyAuthentication()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'name' : ['exact', 'starstwith', 'endswith', 'contains'],
            'date_founded' :['exact', 'lt', 'lte', 'gt', 'gte', 'range'],
            'num_employees' : ['exact', 'lt', 'lte', 'gt', 'gte', 'range'],
            'status' : ['exact'],
            'address' : ['exact', 'contains', 'startswith', 'endswith'],
        }

class GameResource(ModelResource):
    developer = fields.ForeignKey(DeveloperResource, 'developer')
    platforms = fields.ToManyField(PlatformResource, 'platforms')
    class Meta:
        queryset = Game.objects.all()
        resource_name = 'game'
        authentication = ApiKeyAuthentication()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'title' : ['exact', 'starstwith', 'endswith', 'contains'],
            'release_date' : ['exact', 'lt', 'lte', 'gt', 'gte', 'range'],
            'genre' : ['exact', 'starstwith', 'endswith', 'contains'],
            'publisher' : ['exact', 'starstwith', 'endswith', 'contains'],
            'ESRB_rating' : ['exact'],
        }
