# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        # First Name Validations
        if len(postData['first']) < 2: 
            errors.append("First name should be more than 2 characters")
        if not postData['first'].isalpha():
            errors.append("Name cannot contain numbers")

        # Last Name Validation
        if len(postData['last']) < 2:
            errors.append("Last name should be more than 2 characters")
        if not postData['last'].isalpha():
            print 'wizard'

        # Password Validation
        if len(postData['password']) < 8:
            errors.append("Password should be longer than 8 characters")
        if postData['password'] != postData['confirm_password']:
            errors.append("Password do not match")

        #Email Validation
        if len(postData['email']) < 0:
            errors.append("Email must be filled out")
        if len(self.filter(email = postData['email'])) > 1:
            errors.append('Email address is already in use')
        return errors

class User(models.Model):
    first = models.CharField(max_length=255, default = 'blank')
    last = models.CharField(max_length=255, default = 'blank')
    email = models.CharField(max_length=255, default = 'blank')
    password = models.CharField(max_length=255, default = 'blank')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()


class CourseManager(models.Manager):
    def validator(self, postData):

        errors = []
        

  
        
        if len(postData['description']) < 15:
            errors.append("Description must be filled out")

        if len(postData['courseName']) < 5:
            errors.append("Course name must be filled out")
   
        return errors

class Course(models.Model):
    description = models.CharField(max_length=255)
    courseName = models.CharField(max_length=255)
    
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(User, related_name ="userappts")
    favorites = models.ManyToManyField(User, related_name ="userfave")
    objects = CourseManager()