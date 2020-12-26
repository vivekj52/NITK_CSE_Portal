from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Undergraduate, Postgraduate, Doctoral

def courses(request):
    template = loader.get_template('courses.html')
    undergraduate = Undergraduate.objects.all()
    postgraduate = Postgraduate.objects.all()
    doctoral = Doctoral.objects.all()

    context = {
    	'ug' : undergraduate,
    	'pg' : postgraduate,
    	'dc' : doctoral
    }

    return HttpResponse(template.render(context, request))