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
        Qucik test case to get projects
        """

        r = self.client.get("/api/projects/")

        # asserting HTTP OK
        self.assertEquals(r.status_code, 200)

    def test_update_project(self):
        """
        Test case to update a project with REST API
        """

        new_title = "Django Test Project"
        short_name = "DTP"
        path = "/api/projects/%d/" % self.project.id
        data = {"title": new_title, "shortname": short_name,
                "description": "This is some test project",
                "owner": self.user.id}

        r = self.client.put(
                path, json.dumps(data), content_type='application/json')

        # asserting HTTP OK
        self.assertEquals(r.status_code, 200)

        rdata = json.loads(r.content)

        # asserting title and shortname updates
        self.assertEquals(rdata["title"], new_title)
        self.assertEquals(rdata["shortname"], short_name)
