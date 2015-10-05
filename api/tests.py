import requests
import json
import datetime

from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User

from work.models import *

class RestApiTestCase(TestCase):
    """
    test cases for RESTful APIs
    """

    def test_gell_all_projects(self):
        """
        test cases to get JSON for all projects
        """
        url = "http://localhost:8000/api/projects/"
        r = requests.get(url)
        print r.text, r.status_code
        self.assertEqual(r.status_code, 200)

    def test_gell_project_detail(self):
        """
        test case to get project detail by primary key
        """
        url = "http://localhost:8000/api/projects/1"
        r = requests.get(url)
        print r.text, r.status_code
        self.assertEqual(r.status_code, 200)

    def test_gell_all_tasks(self):
        """
        test cases to get JSON for all tasks
        """
        url = "http://localhost:8000/api/tasks/"
        r = requests.get(url)
        print r.text, r.status_code
        self.assertEqual(r.status_code, 200)

