from django.test import TestCase
from django.contrib.auth.models import User

from work.models import Project


class BaseTestCase(TestCase):

    def setUp(self):

        super(BaseTestCase, self).setUp()

        # dummy credentials for success test cases
        self.username = 'navi'
        self.email = 'nsk@gmail.com'
        self.password = 'secret1234'

        # creating test user
        self.user = User.objects.create_user(
                username=self.username, email=self.email,
                password=self.password)

        # creating dummy project
        self.project = Project.objects.create(
                title="Dummy Project",
                shortname="DP", description="This is a dummy project",
                owner=self.user)
