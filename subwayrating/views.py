from subwayrating.models import SubwayStop
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import messages
from comments.models import CommentWithRating
from django.contrib.comments.signals import comment_was_posted
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.http import HttpResponse
from django.template import RequestContext
from serializers import ModelSerializer
from serializers.fields import CharField
import heapq



# Create your views here.  
@csrf_exempt  
def ratings(request):
    cache_key = 'list_of_subways_cache_key'
    cache_time = 3600
    reviews = cache.get(cache_key)
    if not reviews:
        reviews = SubwayStop.objects.all()
        cache.set(cache_key, reviews, cache_time)
    return render_to_response('subwayrating/list.html', {'reviews': reviews}, context_instance = RequestContext(request))

class SubwayStopSerializer(ModelSerializer):
    title = CharField(source='get_title', readonly=True)
    description = CharField(source='slug', readonly=True)

    class Meta:
        model = SubwayStop
        exclude = ('division', 'line', 'name', 'routes', 'latitude', 'longitude', 'wiki_url', 'mta_url', 'misc_url', 'slug', 'enable_comments')
        
def get_subway_stops(request):
    cache_key = 'list_of_subways_cache_key'
    cache_time = 3600
    reviews = cache.get(cache_key)
    if not reviews:
        reviews = SubwayStop.objects.all()
        cache.set(cache_key, reviews, cache_time)
    data = SubwayStopSerializer().serialize('json', reviews, context = RequestContext(request))
    return HttpResponse(data, mimetype='application/json')
    
        
def view_comment(request, slug):
        return render_to_response('subwayrating/view_comment.html', {
        'stop_comment': get_object_or_404(SubwayStop, slug=slug)
    }, context_instance = RequestContext(request))
     
        
def top_n_stops(request):
    reviews = SubwayStop.objects.all()
    return render_to_response('subwayrating/topn.html', {'reviews': heapq.nlargest(5, reviews)}, context_instance=RequestContext(request))

def bottom_n_stops(request):
    reviews = SubwayStop.objects.all()
    return render_to_response('subwayrating/topn.html', {'reviews': heapq.nsmallest(5, reviews)}, context_instance=RequestContext(request))

def comment_messages(sender, comment, request, **kwargs):
    if request.user.is_authenticated():
        messages.add_message(
            request,
            messages.SUCCESS,
            _('Thank you for your comment!')
        )
    else:
        messages.add_message(
            request,
            messages.INFO,
            _('No comments without authentication')
        )
        
        
comment_was_posted.connect(comment_messages, sender=CommentWithRating)
        
    
    