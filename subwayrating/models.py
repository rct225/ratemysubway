from django.db import models
from django.db.models import permalink
from comments.models import CommentWithRating, CommentManager



# Create your models here.

class SubwayStop(models.Model):
    division = models.CharField(max_length=10)
    line = models.CharField(max_length=100) 
    name = models.CharField(max_length=200)
    routes = models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    enable_comments = models.BooleanField()
    
    rating = CommentWithRating()
    
    objects = CommentManager()
        
    def __unicode__(self):
        return self.name

    
    @permalink
    def get_absolute_url(self):
        return('view_stop', None, { 'slug' : self.slug})
    
    
    
    
    
    
