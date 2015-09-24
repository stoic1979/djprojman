from django.db import models


class Project(models.Model):
    """
    project model for weavebytes
    """
    title        = models.CharField(max_length=64)
    description  = models.CharField(max_length=1024)
    start        = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """
        function returns unicode/string representation of a project model
        """
        return "Project:: %s" % self.title

class Employee(models.Model):
    """
    employee model for weavebytes
    """
    username     = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    email        = models.CharField(max_length=45)
    password     = models.CharField(max_length=45)
    last_login   = models.DateTimeField()

    def __unicode__(self):
        """
        function returns unicode string representation of model
        """
        return "Weavebytes Employee:: %s" % self.username
