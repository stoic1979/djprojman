import traceback

from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from work.models import *
from dashboard.forms import LoginForm, AddProjectForm, AddTaskForm, AddTodoForm
from django.core.context_processors import csrf

def get_common_dict(request):
    """
    common params to be passed in the dict to all views/pages
    """
    c = {'projects': Project.objects.all(),
            'request': request,
            'frmAddProject': AddProjectForm(),
            'frmAddTask': AddTaskForm(),
            'frmAddTodo': AddTodoForm()}
    return c

@login_required
def home(request):
    """
    home page view for the website
    """
    return render_to_response('index.html', get_common_dict(request), context_instance=RequestContext(request))

def login_page(request):
    """
    If user is authenticated, direct them to the next page. 
    Otherwise, take them to the login page.

    :param request: django HttpRequest

    :return: django HttpResponse 
    """

    print "--- login --"

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
    return render_to_response('help.html')

@login_required
def progress(request):
    """
    show progress page
    """
    return render_to_response('progress.html', get_common_dict(request), context_instance=RequestContext(request))

@login_required
def tasks(request):
    """
    show page for adding a task
    """
    return render_to_response('tasks.html', get_common_dict(request))

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

    return HttpResponseRedirect('/', get_common_dict(request))

@login_required
def project(request, project_id):
    """
    get all tasks for given project
    """
    project = Project.objects.get(id=project_id)
    c = get_common_dict(request)
    d = {'project': project, 'tasks': project.get_tasks()}
    c.update(d)
    return render_to_response('tasks.html', c)

@login_required
def task_detail(request, task_id):
    """
    show task details
    """
    task = Task.objects.get(id=task_id)
    c = get_common_dict(request)
    d = {'task': task, 'comments': task.get_comments()}
    c.update(d)
    return render_to_response('task_detail.html', c)

@csrf_exempt
@login_required
def save_task(request):
    """
    save task in db
    """
    try:
        title       = request.POST['title']
        description = request.POST["description"]
        project_id  = request.POST["project_id"]
        type        = request.POST["type"]

        print "project_id=", project_id
        # getting project for this task by project id
        project = Project.objects.get(id=int(project_id))

        # saving task
        task = Task(project=project, title=title, type=type, description=description, worker=request.user)
        task.save()
    except:
        traceback.print_exc()
        return HttpResponse(" Failed To Save Task !")

    # redirecting to the project's page where all tasks etc is shown
    return HttpResponseRedirect('/project/%s' % project_id, get_common_dict(request))

@csrf_exempt
@login_required
def save_todo(request):
    """
    save user's todo
    """
    try:
        note = request.POST['note']
        done = False

        snote = Stickynote(note=note, done=done, user=request.user)
        snote.save()
    except:
        traceback.print_exc()
        return HttpResponse(" Failed To Save Todo !")

    return HttpResponseRedirect('/', get_common_dict(request))
