from django.db import models

#
# A project has tasks, and a task is assigned to an worker
# 
# Company will have serveral projects to be managed
#

class Project(models.Model):
    """
    project model for the company
    """
    title        = models.CharField(max_length=64)
    description  = models.CharField(max_length=1024)
    start_date   = models.DateField()

    def __unicode__(self):
        """
        function returns unicode representation of a project
        """
        return "Project:: %s" % self.title

class Worker(models.Model):
    """
    worker model for the company
    """
    username     = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    email        = models.CharField(max_length=45)
    password     = models.CharField(max_length=45)
    last_login   = models.DateTimeField()

    def __unicode__(self):
        """
        function returns unicode representation of a worker
        """
        return "Worker:: %s" % self.username

class Task(models.Model):
    """
    task model for the company
    """
    title       = models.CharField(max_length = 64)
    description = models.TextField(null=True, blank=True)
    project     = models.ForeignKey('Project')
    start_date  = models.DateField()
    end_date    = models.DateField()
    worker      = models.ForeignKey('Worker', null=True)
    completed   = models.BooleanField(default=False)
	
    def __unicode__(self):
	    """
	    function returns unicode representaion of a task
	    """
	    return "Task:: %s" % self.name

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
    task        = models.ForeignKey('Task')
    write_date  = models.DateField()
    worker      = models.ForeignKey('Worker', null=True)
    screenshot  = models.TextField(null=True, blank=True)
	
    def __unicode__(self):
	    """
	    function returns unicode representaion of a comment
	    """
	    return "Comment:: %s" % self.comment

