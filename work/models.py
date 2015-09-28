from django.contrib.auth.models import User
from django.db import models
import datetime

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
    description  = models.CharField(max_length=1024)
    owner        = models.ForeignKey(User)
    start_date   = models.DateField(default=datetime.date.today)
    end_date     = models.DateField(null=True)
    is_active    = models.BooleanField(default=True)

    def __unicode__(self):
        """
        function returns unicode representation of a project
        """
        return self.title

class Task(models.Model):
    """
    task model for the company
    """
    title       = models.CharField(max_length = 64)
    description = models.TextField(null=True, blank=True)
    project     = models.ForeignKey(Project)
    start_date  = models.DateField()
    end_date    = models.DateField()
    worker      = models.ForeignKey(User, null=True)
    completed   = models.BooleanField(default=False)
	
    def __unicode__(self):
	    """
	    function returns unicode representaion of a task
	    """
	    return self.title

class Comment(models.Model):
    """
    comment model for the company

    A task can have several comments with title, description
    and screenshot

    FIXME:
        A the moment, adding only one screenshot per comment !
    """
    title       = models.CharField(max_length = 64)
    description = models.TextField(null=True, blank=True)
    task        = models.ForeignKey(Task)
    write_date  = models.DateField()
    worker      = models.ForeignKey(User, null=True)
    screenshot  = models.TextField(null=True, blank=True)
	
    def __unicode__(self):
	    """
	    function returns unicode representaion of a comment
	    """
	    return self.title

