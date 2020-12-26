from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Workshops, Conferences, News



def events(request):
    template = loader.get_template('events.html')
    workshops = Workshops.objects.all()
    conferences = Conferences.objects.all()
    news = News.objects.all()
    
    context = {
    	'ws':workshops,
    	'cf':conferences,
    	'ne':news
    }

    return HttpResponse(template.render(context, request))
    