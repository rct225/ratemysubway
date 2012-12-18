from subwayrating.models import SubwayStop
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from comments.models import CommentWithRating
from django.contrib.comments.signals import comment_was_posted
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
import heapq



# Create your views here.  
@requires_csrf_token  
def ratings(request):
    reviews = SubwayStop.objects.all()
    return render_to_response('subwayrating/list.html', {'reviews': reviews}, context_instance=RequestContext(request))

def view_comment(request, slug):
        return render_to_response('subwayrating/view_comment.html', {
        'stop_comment': get_object_or_404(SubwayStop, slug=slug)
    }, context_instance=RequestContext(request))
     
        
def top_n_stops(request):
    reviews = SubwayStop.objects.all()
    return render_to_response('subwayrating/list.html', {'reviews': heapq.nlargest(5, reviews)}, context_instance=RequestContext(request))

def bottom_n_stops(request):
    reviews = SubwayStop.objects.all()
    return render_to_response('subwayrating/list.html', {'reviews': heapq.nsmallest(5, reviews)}, context_instance=RequestContext(request))

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
        
    
    