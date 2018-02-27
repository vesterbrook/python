# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be more than 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be more than 2 characters"    
        if len(postData['email']) < 5:
            errors["email"] = "Email should be longer"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255, default = 'blank')
    last_name = models.CharField(max_length=255, default = 'blank')
    email = models.CharField(max_length=255, default = 'blank')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()