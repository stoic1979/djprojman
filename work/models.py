from django.db import models

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
