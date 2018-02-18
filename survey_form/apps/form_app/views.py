# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    print "working"

    return render(request, "form_app/index.html")


def process(request):

    if 'counter' in request.session:
        request.session['counter'] +=1
    else:    
        request.session['counter'] = 1

    context = {
        "name" : request.POST['name'],
        "location" : request.POST['location'],
        "language" : request.POST['language'],
        "comment" : request.POST['comment']

    }

    return render(request, "form_app/submit.html", context)



def show(request):


    return redirect('/')