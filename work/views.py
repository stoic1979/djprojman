import traceback

from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from work.models import *

def home(request):
    """
    home page view for the website
    """
    return render_to_response('index.html')

@csrf_exempt
def add_project(request):
    """
    show page for adding a project
    """
    return render_to_response('add_project.html')

@csrf_exempt
def save_project(request):
    """
    save project in db
    """
    try:
        title       = request.POST['title']
        description = request.POST["description"]

        project = Project(title=title, description=description)
        project.save()
    except:
        traceback.print_exc()
        return HttpResponse(" Failed To Save Project !")

    return HttpResponse(" Project Saved !")
