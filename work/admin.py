from django.contrib import admin

from work.models import *

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Stickynote)
