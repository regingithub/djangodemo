from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import CharField,DateField
from datetime import date
    
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    DOB = models.CharField(max_length=10)
    join_date = models.CharField(max_length=10)
    emp_department = models.ForeignKey('Department',on_delete=models.DO_NOTHING,null=True)
    emp_manager = models.ForeignKey('Employee',on_delete=models.DO_NOTHING,null=True)
    
class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    dep_manager = models.ForeignKey(Employee,on_delete=models.DO_NOTHING,null=True)
    
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
    
    
    
