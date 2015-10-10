# djprojman
A project management tool in django. 
Intents to be a simple quick tool for managing projects, tasks and team, most suitable for small companies.

Under R&D by weavebytes.


Features
--------

* Each project will have tasks and workers to handle them. 
* Each task can have several comments by worker.
* Comments will have title, description and screenshots.
* There is a UI to add/edit/manage tasks.
* There is a UI to add/edit/manage comments.


Unit Tests
--------

* Run tests as:-
 $ python manage.py test --keepdb

Setup Instructions
--------

* simple captcha

 - You must install following dependencies:-
    apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev

 - Then installing simple catcha with:-
    pip install Pillow
    pip install django-simple-captcha

 - For more details, follow simple captcha docs:-
   http://django-simple-captcha.readthedocs.org/en/latest/usage.html

* django rest framework

 - pip install djangorestframework
 - pip install markdown
 - pip install django-filter

 - For more details, follow django rest framework docs:-
    http://www.django-rest-framework.org/

* grappelli - for admin skinning

 - pip install django-grappelli

 - Open settings.py and add grappelli to your INSTALLED_APPS (before django.contrib.admin):

    INSTALLED_APPS = (
        'grappelli',
        'django.contrib.admin',
    )

 - For more details, follow grappelli docs:-
    http://django-grappelli.readthedocs.org/en/latest/quickstart.html#installation

$ python manage.py collectstatic


Testing RESTful APIs
--------

* Get all projects
 - http://localhost:8000/api/projects/

ToDo
--------

* Create template system to set desired theme.
* Create graphs to show progress of projects.
