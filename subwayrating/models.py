from django.db import models
from django.db.models import permalink
from comments.models import CommentWithRating
from django.contrib.comments.moderation import CommentModerator, moderator


# Create your models here.


class SubwayStop(models.Model):
    division = models.CharField(max_length=10)
    line = models.CharField(max_length=100) 
    name = models.CharField(max_length=200)
    routes = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    wiki_url = models.CharField(max_length=1000)
    mta_url = models.CharField(max_length=1000)
    misc_url = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=100)
    enable_comments = models.BooleanField()
    
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    rating = CommentWithRating()
        
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(SubwayStop, self).save(*args, **kwargs)
        self.average_rating = self.compute_average_rating()
        
    def get_title(self):
        title = self.name + '(' + self.line + ')'
        return title

    def compute_average_rating(self):
        ratings = CommentWithRating.objects.for_model(self)
        ratings_count = ratings.count()
        if ratings_count == 0:
            ratings_count = 1
        rating_sum = 0
        for rating in ratings:
            rating_sum = rating_sum + rating.rating
        return round((rating_sum / ratings_count), 2)
    
    def get_average_rating(self):
        if self.average_rating == None:
            self.average_rating = self.compute_average_rating()          
        return self.average_rating;
    
    def __lt__(self, other):
        return self.get_average_rating() < other.get_average_rating()
    
    @permalink
    def get_absolute_url(self):
        return('view_stop', None, { 'slug' : self.slug})
    
class SubwayStopModerator(CommentModerator):
    email_notification = False
    enable_field = 'enable_comments'
    moderate_after = 0
    
    def moderate(self, comment, content_object, request):
        if comment.user and comment.user.is_authenticated():
            return False
        else:
            return True
        
        
if SubwayStop not in moderator._registry:
    moderator.register(SubwayStop, SubwayStopModerator)
    
    
    
    
    
    
