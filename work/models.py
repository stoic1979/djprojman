from django.contrib.auth.models import User
from django.db import models
import datetime

from tinymce.models import HTMLField

#
# A project has tasks, and a task is assigned to an worker
# 
# Company will have several projects to be managed
#

class Project(models.Model):
    """
    project model for the company
    """
    title        = models.CharField(max_length=64)
    shortname    = models.CharField(max_length=20, unique=True)
    description  = HTMLField()
    owner        = models.ForeignKey(User)
    start_date   = models.DateField(default=datetime.date.today)
    end_date     = models.DateField(null=True)
    is_active    = models.BooleanField(default=True)

    def __unicode__(self):
        """
        function returns unicode representation of a project
        """
        return self.title

    def get_tasks(self):
        """
        function get all tasks belonging to this project
        """
        return Task.objects.filter(project=self)

class Task(models.Model):
    """
    task model for the company
    """
    title       = models.CharField(max_length=64)
    type        = models.CharField(max_length=64, default='Task')
    priority    = models.CharField(max_length=64, default='Major')
    description = HTMLField()
    project     = models.ForeignKey(Project)
    start_date  = models.DateField(default=datetime.date.today)
    end_date    = models.DateField(null=True)
    worker      = models.ForeignKey(User, null=True)
    hours_taken = models.PositiveIntegerField(default=0)
    completed   = models.BooleanField(default=False)
	
    def __unicode__(self):
	"""
	function returns unicode representaion of a task
	"""
	return self.title

    def get_comments(self):
        """
        function get all comments belonging to this task
        """
        return Comment.objects.filter(task=self)

class Comment(models.Model):
    """
    comment model for the company

    A task can have several comments with title, description
    and screenshot

    FIXME:
        A the moment, adding only one screenshot per comment !
    """
    title       = models.CharField(max_length = 64)
    description = HTMLField()
    task        = models.ForeignKey(Task)
    write_date  = models.DateField(default=datetime.date.today)
    worker      = models.ForeignKey(User, null=True)
    screenshot  = models.TextField(null=True, blank=True)
	
    def __unicode__(self):
	"""
	function returns unicode representaion of a comment
	"""
	return self.title


class Stickynote(models.Model):
    """
    user specific sticky note

    Each user can have his/her own sticky notes :)
    """
    user       = models.ForeignKey(User)
    note       = models.CharField(max_length=128)
    done       = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
	"""
	function returns unicode representaion of a sticky note
	"""
	return self.note
