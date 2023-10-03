from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def experiments(request):
    template = loader.get_template('experiments.html')
    return HttpResponse(template.render({}, request))
