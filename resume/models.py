from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    skillDetail = models.TextField(default='')
    academic_detail = models.TextField(default='')
    area_of_interest_detail = models.TextField(default='')
    degree = models.CharField(max_length=50)
    stream = models.CharField(max_length=100)
    passing_year = models.TextField(default='')
    result = models.CharField(max_length=5)
    work = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    start_date = models.TextField(default='')
    end_date = models.TextField(default='')
    description = models.TextField(default='')
    def full_name(self):
        return " ".join([self.first_name, self.last_name])
