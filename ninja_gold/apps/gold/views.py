# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []

    return render(request, 'gold/index.html')


def money(request):

    if request.POST['action'] == 'farm':
        gamble = random.randrange(10, 21)
        request.session['gold_count'] += farm_add
        string = "You have earned " + str(farm_add) + " golds from the farm. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)
    elif request.POST['action'] == 'cave':
        gamble = random.randrange(5, 11)
        request.session['gold_count'] += cave_add
        string = "You have earned " + str(cave_add) + " golds from the cave. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)
    elif request.POST['action'] == 'house':
        gamble = random.randrange(2, 6)
        request.session['gold_count'] += house_add
        string = "You have earned " + str(house_add) + " golds from the house. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session['activity_log'].append(string)
    elif request.POST['action'] == 'casino':
        casino_chance = random.randint(1,2)
        if luck == 1:
            gamble = random.randrange(1, 50)
            request.session['gold_count'] += casino_add
            string = "You have earned " + str(casino_add) + " golds from the casino. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            request.session['activity_log'].append(string)
        elif casino_chance == 2:
            gamble = random.randint(-50,0)
            request.session['gold_count'] += casino_add
            string = "Entered a casino and lost " + str(casino_add) + " golds... Ouch! " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            request.session['activity_log'].append(string)
    
    
    
    return redirect('/')




def reset(reqeust):
    request.session.clear()
    return redirect('/')