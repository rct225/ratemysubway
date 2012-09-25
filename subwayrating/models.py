from django.db import models
from django.db.models import permalink
from comments.models import CommentWithRating


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
        
    def __unicode__(self):
        return self.name

    def get_average_rating(self):
        ratings = CommentWithRating.objects.for_model(self)
        ratings_count = ratings.count()
        if ratings_count == 0:
            ratings_count = 1
        rating_sum = 0
        for rating in ratings:
            rating_sum = rating_sum + rating.rating
        return rating_sum / ratings_count
    
    def __lt__(self, other):
        return self.get_average_rating() < other.get_average_rating()
    
    @permalink
    def get_absolute_url(self):
        return('view_stop', None, { 'slug' : self.slug})
    
    
    
    
    
    
