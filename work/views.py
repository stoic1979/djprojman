import traceback

from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from work.models import *
from dashboard.forms import LoginForm
from django.core.context_processors import csrf

@login_required
def home(request):
    """
    home page view for the website
    """
    return render_to_response('index.html', {'request':request})

def login_page(request):
    """
    If user is authenticated, direct them to the next page. 
    Otherwise, take them to the login page.

    :param request: django HttpRequest

    :return: django HttpResponse 
    """

    state = ""
    username = password = ''
    form = LoginForm()

    #default next page is index page
    next_page = "/"

    #getting next page in get request
    if request.GET:
        next_page = request.GET.get('next')

    if request.POST:
        form = LoginForm(request.POST) # A form bound to the POST data
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect(next_page) # Redirect after POST
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    c = {'state':state, 'username': username, 'form': form, 'next': next_page}
    c.update(csrf(request)) 

    return render_to_response('auth.html', c)

def logout_page(request):
    """ Log users out and re-direct them to the main page. """
    logout(request)
    return HttpResponseRedirect('/login/', {'request':request})

@login_required
def help(request):
    """
    show help page
    """
    #return render_to_response('add_project.html')
    return HttpResponse('Help Page')

@csrf_exempt
@login_required
def add_project(request):
    """
    show page for adding a project
    """
    return render_to_response('add_project.html', {'request':request})

@csrf_exempt
@login_required
def save_project(request):
    """
    save project in db
    """
    try:
        title       = request.POST['title']
        shortname   = request.POST["shortname"]
        description = request.POST["description"]

        project = Project(title=title, shortname=shortname, description=description, owner=request.user)
        project.save()
    except:
        traceback.print_exc()
        return HttpResponse(" Failed To Save Project !")

    return HttpResponse(" Project Saved !")
