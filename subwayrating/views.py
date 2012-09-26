from subwayrating.models import SubwayStop
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
import heapq



# Create your views here.
def index(request):
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
        
    
    