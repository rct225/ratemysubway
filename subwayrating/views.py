from subwayrating.models import SubwayStop
from django.shortcuts import render_to_response, get_object_or_404
#from django.template import Context, loader
from django.template import RequestContext
#from django.contrib import messages
#from django.contrib.comments import Comment
#from django.contrib.comments.signals import comment_was_posted
#from django.utils.translation import ugettext as _
from comments.models import CommentWithRating


# Create your views here.
def index(request):
    reviews = SubwayStop.objects.all()
    return render_to_response('subwayrating/list.html', {'reviews': reviews}, context_instance=RequestContext(request))

def view_comment(request, slug):
    average_rating = CommentWithRating.objects.for_model(SubwayStop.objects.get(slug=slug)).count()
    return render_to_response('subwayrating/view_comment.html', {
        'stop_comment': get_object_or_404(SubwayStop, slug=slug), 'average_rating': average_rating
    }, context_instance=RequestContext(request))
    
    