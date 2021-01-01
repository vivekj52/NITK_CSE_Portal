from django.http import HttpResponse
from django.template import loader

# Create your views here.


def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))


def programmes(request):
    template = loader.get_template('programmes.html')
    context = {}
    return HttpResponse(template.render(context, request))


def facilities(request):
    template = loader.get_template('facilities.html')
    context = {}
    return HttpResponse(template.render(context, request))


def placements(request):
    template = loader.get_template('placements.html')
    context = {}
    return HttpResponse(template.render(context, request))
