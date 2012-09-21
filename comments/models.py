from django.db import models
from django.contrib.comments.models import Comment
from django.contrib.comments.managers import CommentManager
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode

#from django.db.models import Avg

# Create your models here.
class CommentManager(CommentManager):
        def in_moderation(self):
            """ QuerySet for all comments currently in the moderation queue. """
            return self.get_query_set().filter(is_public=False, is_removed=False)

        def for_model(self, model):
            """
            QuerySet for all comments for a particular model (either an instance or
            a class).
            """
            ct = ContentType.objects.get_for_model(model)
            qs = self.get_query_set().filter(content_type=ct)
            if isinstance(model, models.Model):
                qs = qs.filter(object_pk=force_unicode(model._get_pk_val()))
            return qs
    
class CommentWithRating(Comment):
    rating = models.IntegerField()
    
    objects = CommentManager()
    
    
    # def save(self, *args, **kwargs):
        # self.content_object.rating.add(score=self.rating, user=self.user, ip_address=self.ip_address)
        # super(CommentWithRating, self).save(*args, **kwargs)
 
    
