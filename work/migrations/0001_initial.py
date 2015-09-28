# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(null=True, blank=True)),
                ('write_date', models.DateField()),
                ('screenshot', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('shortname', models.CharField(unique=True, max_length=20)),
                ('description', models.CharField(max_length=1024)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(null=True, blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(to='work.Project')),
                ('worker', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(to='work.Task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='worker',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
