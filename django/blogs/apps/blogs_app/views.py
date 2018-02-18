# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }

    request.session['name'] = request.POST['name']
    request.session['counter'] = 100

    return render(request, "blogs_app/index.html", context)

def new(request):
    response= "placeholder to create new blog"

    return HttpResponse(response)

def create(request):

    if request.method == "POST":
	    print "*"*50
	    print request.POST
            print request.POST['name']
            print request.POST['desc']
            request.session['name'] = "test"  # more on session below
	    print "*"*50
	    return redirect("/")
    else:
	    return redirect("/")

    

def show(request, number):
    response="placeholder to display blog "
    
    return HttpResponse(response + number)

def edit(request, number):
    response="placeholder to edit blog " 

    return HttpResponse(response + number)

def destroy(request):
    
    return redirect('/')

   

