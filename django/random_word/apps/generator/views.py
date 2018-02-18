# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string



def index(request):
    print "im here"
    return render(request, "generator/index.html")


def rando(request):


    if 'counter' in request.session:
        request.session['counter'] +=1
    else:    
        request.session['counter'] = 1
    unique_id = get_random_string(length=14)
    words = {
        "something" : unique_id
    }



    return render(request, 'generator/index.html', words)


def reset(request):

    request.session.clear()

    
    return redirect('/')