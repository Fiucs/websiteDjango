# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ActionMovie(models.Model):
    line_num = models.AutoField(primary_key=True)
    mv_name = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action_movie'


class ActionMovie1(models.Model):
    line_num = models.AutoField(primary_key=True)
    mv_name = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action_movie1'


class ActionMovieCopy(models.Model):
    line_num = models.AutoField(primary_key=True)
    mv_name = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action_movie_copy'


class ComedyMovie(models.Model):
    line_num = models.AutoField(primary_key=True)
    mv_name = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comedy_movie'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class HorrorMovie(models.Model):
    line_num = models.AutoField(primary_key=True)
    mv_name = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=900, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horror_movie'


class ScienceMovie(models.Model):
    line_num = models.AutoField(primary_key=True)
    mv_name = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=900, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'science_movie'


class StoryMovie(models.Model):
    line_num = models.AutoField(primary_key=True)
    mv_name = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'story_movie'


