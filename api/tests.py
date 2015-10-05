import requests
import json
import datetime

from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User

from work.models import *


def send_http_request(url, payload):
    """
    function to send http request to server

    returns tuple with HTTP status code and JSON response
    from the server
    """

    content_type = "application/%s" % format
    headers = {'content-type': content_type}

    r = requests.post(url, data=payload, verify=True)

    print "Server Response: ", r.text

    resp = json.loads(r.text)
    return r.status_code, resp

class RestApiTestCase(TestCase):

    def test_gell_all_projects(self):
        url = "http://localhost:8000/api/projects/"
        r = requests.get(url)
        print r.text, r.status_code
        self.assertEqual(r.status_code, 200)

