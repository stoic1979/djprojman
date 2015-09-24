from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

def home(request):
    """
    home page view for the website
    """
    #return HttpResponse("<b>Weavebytes Hospital</b>")
    return render_to_response('index.html')
