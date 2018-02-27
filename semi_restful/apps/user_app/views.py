# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import User

def index(request):
    context = {
        'users' : User.objects.all()
    }

    return render (request, 'user_app/index.html', context)

def new(request):

    return render(request, 'user_app/new_user.html')

def edit(request, id):

    person = User.objects.get(id=id) 

    context = {
         'person' : person
     }

    return render(request, 'user_app/edit.html', context)

def show(request, id):

    print ('THIS IS ME SHOWING YOU STUFF!!!!!')
    user = User.objects.get(id=id) #QUERY to get the id of the specific person to be displayed
    context = {
        'user': user
        
     } #Dictionary containing user information for use in this template/view
    return render(request, 'user_app/show.html', context) #Renders a template and CONTEXT is stated here because you want to pass that info onto the template

  

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors.iteritems():
            messages.error(request, error)
        
        return redirect('/users/new')
    else:
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email']
        )
        return redirect('/')



def destroy(request, id):
    print "delete is working"
    user = User.objects.filter(id=id)
    user.delete()
    return redirect('/')

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect('edit/'.format(id))
    else:
        user = User.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        
    
        return redirect('/show/'+id)



