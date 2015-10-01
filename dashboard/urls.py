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
    url(r'^add_project/$', 'work.views.add_project', name='add_project'),
    url(r'project/(\d+)$', 'work.views.project', name='project'),
    url(r'^tasks/$', 'work.views.tasks', name='tasks'),
    url(r'^save_project/$', 'work.views.save_project', name='save_project'),
    url(r'^help/$', 'work.views.help', name='help'),
    url(r'^login/$', 'work.views.login_page', name='login_page'),
    url(r'^logout/$', 'work.views.logout_page', name='logout_page'),
    url(r'^accounts/logout/$', 'work.views.logout_page', name='logout_page'),
    url(r'^accounts/login/$', 'work.views.login_page', name='login_page'),
    url(r'^progress/$', 'work.views.progress', name='progress'),
]
