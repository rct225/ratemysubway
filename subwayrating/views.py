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
    # ratings = CommentWithRating.objects.for_model(SubwayStop.objects.get(slug=slug))
    # rating_sum = 0
    # for rating in ratings:
        # rating_sum = rating_sum + rating.rating
    # average_rating = rating_sum / ratings.count()
    # return render_to_response('subwayrating/view_comment.html', {
        # 'stop_comment': get_object_or_404(SubwayStop, slug=slug), 'average_rating': average_rating
    # }, context_instance=RequestContext(request))
        return render_to_response('subwayrating/view_comment.html', {
        'stop_comment': get_object_or_404(SubwayStop, slug=slug)
    }, context_instance=RequestContext(request))
    
    