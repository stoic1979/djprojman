import json

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from base import BaseTestCase

class RestApiTestCase(BaseTestCase):
    """ Test cases for RESTful APIs """

    def setUp(self):
        """
        setup tests
        """
        super(RestApiTestCase, self).setUp()

    def get_api_list(self):
        """ 
        convenience function to get list of all api
        """
        c = Client()
        r = c.get('/api/')
        print "API List:", r.content

    def test_get_projects(self):
        """ 
        Test case with a valid user and gets token succesfully
        """

        r = self.client.get("/api/projects/")
        print "[test_rest_apis] test_get_projects() :: resp code =", r.status_code

        # asserting HTTP OK
        self.assertEquals(r.status_code, 200)

        print r.content
