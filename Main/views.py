from django.shortcuts import render
from django.http import HttpResponseRedirect

from researcher import data
from researcher import write_data
from researcher import learn_data

def index(request):
    return render(request, 'EarthTrackerIndex.html')

def loadData(request):
    data.retrieve_All()

    return HttpResponseRedirect('/')

def writeData(request):
    write_data.write_All()

    return HttpResponseRedirect('/')

def learnData(request):
    learn_data.learn_all()

    return HttpResponseRedirect('/')