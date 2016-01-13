import datetime
from django.test import TestCase

from work.models import Project

today_date = datetime.date.today()
today_str  = str(today_date)

class ProjectTestCase(BaseTestCase):

    user    = None
    project = None

    def setUp(self):
        """
        create a test user and a project for test cases
        """
        # creating dummy user
        self.user = User.objects.create_user('Dummy', 'dummy@gmail.com', 'dummy')

        # creating dummy project
        self.project = Project.objects.create(title="Dummy Project", shortname="DP", description="This is a dummy project", owner=self.user)
        print "Project created"

    def test_required_fields(self):
        """
        sanity tests to check that required fields are really required
        """
        # empty project
        project = Project()
        self.assertRaises(Exception, project.save)

        # adding title
        project.title = 'Dummy Project'
        self.assertRaises(Exception, project.save)

        # adding description
        project.description = 'Dummy Project Under Development'
        self.assertRaises(Exception, project.save)

        # adding shortname/alias
        project.shortname = 'DUMMY'
        self.assertRaises(Exception, project.save)

        # adding start_date
        project.start_date = datetime.date.today()
        self.assertRaises(Exception, project.save)

        # adding owner
        project.owner = self.user
        project.save()

    def test_project_title(self):
        """
        test that project title is not empty
        """
        project = Project(shortname='TP', owner=self.user, description="This is a test project")
        project.title = ''
        self.assertRaises(Exception, project.save)
        project.title = 'Test Project'
        project.save()

    def test_short_name_unique(self):
        """
        in models we have declared that short name is unique

        lets, test that shortnames are unqiue
        """

        # creating project
        project1 = Project(shortname='ABC', title='ABC Project', owner=self.user, description="Some another project")
        project1.save()

        # creating project with same shortname/alias
        project2 = Project(shortname='ABC', title='ABC Project', owner=self.user, description="Some another project")
        self.assertRaises(Exception, project2.save)

    def tearDown(self):
        """
        cleanup saved/dummy data etc
        """
        if self.project:
            self.project.delete()
        if self.user:
            self.user.delete()
