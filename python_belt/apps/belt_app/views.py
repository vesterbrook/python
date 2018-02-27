# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.messages import error
from .models import *
from time import gmtime, strftime
from datetime import datetime
import bcrypt
import re

# Create your views here.
def index(request):
    return render(request, 'belt_app/index.html')

def register(request):
    print ('REGISTER VIEW')
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.create(
            first = request.POST['first'],
            last = request.POST['last'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        request.session['user_id'] = user.id
        context = {
            'user' : user
        }
    return render(request, 'belt_app/success.html', context)

def login(request):
    print('LOGIN VIEW')
    errors = []
    try:
        u = User.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), (User.objects.filter(email=request.POST['email']))[0].password.encode()) == True:  
            print 'wizard'
            request.session['user_id'] = u.id 
            user = User.objects.get(id=u.id)
            return redirect('/success')
        else:
            errors.append('Invalid Password!')
    except:
        errors.append('Email does not exist!')
    print 'muggle'
    for error in errors:
        messages.error(request, error)
    return redirect('/')


def create(request):
    errors = Appoint.objects.validator(request.POST)

    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/success')
    else:
        user = User.objects.get(id=request.session['user_id'])
        appoint = Appoint.objects.create(   
            apptask = request.POST['apptask'],
            apptime = request.POST['apptime'],
            appdate = request.POST['appdate'], 
            creator = user
         )
 
    return redirect('/success')

def success(request):
    print('SUCCESS VIEW')
    today = datetime.now().date()
    user = User.objects.get(id=request.session['user_id'])
    appoint = Appoint.objects.filter(creator=user).filter(appdate=today)
    appoint1 = Appoint.objects.exclude(appdate=today).filter(creator=user)
    context = {
        
        'user' : user,
        'appoint' : appoint,
        'appoint1' : appoint1
    }
    return render(request, 'belt_app/success.html', context)

def logout(request):
    print('YOU IS LOGGED OUT BITCH')
    try:
        print ('TRY LOGOUT')
        del request.session['user_id']
    except KeyError:
        print ('EXCEPT LOGOUT')
        pass
    return redirect('/')

def edit(request, id):

    user = User.objects.get(id=request.session['user_id'])
    appoint = Appoint.objects.get(id=id) 

    context = {
        
        
        'user' : user,
        'appoint' : appoint,
        }
    print appoint.id
    return render(request, 'belt_app/edit.html', context)


def update(request, id):
    errors = Appoint.objects.validator(request.POST)
    if errors:
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect('/edit')

    else:
        appoint = Appoint.objects.get(id = id)
        appoint.apptask = request.POST['apptask']
        appoint.appdate = request.POST['appdate']
        appoint.appstatus = request.POST['appstatus']
        appoint.apptime = request.POST['apptime']
        appoint.save()


    return redirect('/success')

def destroy(request, id):
    print "delete is working"
    appoint = Appoint.objects.filter(id=id)
    appoint.delete()
    return redirect('/success')

