from subwayrating.models import SubwayStop
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader
from django.template import RequestContext
from django.contrib import messages
from django.contrib.comments import Comment
from django.contrib.comments.signals import comment_was_posted
from django.utils.translation import ugettext as _



# Create your views here.
def view_comment(request, slug):
    return render_to_response('subwayrating/view_comment.html', {
        'stop_comment': get_object_or_404(SubwayStop, slug=slug)
    }, context_instance=RequestContext(request))
    
    