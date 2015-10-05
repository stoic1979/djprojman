"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'work.views.home', name='home'),
    url(r'project/(\d+)$', 'work.views.project', name='project'),
    url(r'^tasks/$', 'work.views.tasks', name='tasks'),
    url(r'task_detail/(\d+)$', 'work.views.task_detail', name='task_detail'),
    url(r'^save_project/$', 'work.views.save_project', name='save_project'),
    url(r'^login/$', 'work.views.login_page', name='login_page'),
    url(r'^logout/$', 'work.views.logout_page', name='logout_page'),
    url(r'^accounts/logout/$', 'work.views.logout_page', name='logout_page'),
    url(r'^accounts/login/$', 'work.views.login_page', name='login_page'),
    url(r'^progress/$', 'work.views.progress', name='progress'),

    # 'registration.views.registration_form' view
    url(r'register/$', 'registration.views.registration_form'),
      
    # Allow the URLs beginning with /captcha/ to be handled by
    # the urls.py of captcha module from 'django-simple-captcha'
    url(r'^captcha/', include('captcha.urls')),

    # url conf for rest framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
