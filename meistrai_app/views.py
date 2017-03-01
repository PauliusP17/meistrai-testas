from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Picture


def index(request):
    template = loader.get_template('meistrai_app/home.html')
    return HttpResponse(template.render(context=None, request=request))


def gallery(request):
    template = loader.get_template('meistrai_app/gallery.html')
    images = Picture.objects.order_by('-id')
    context = {
        'images': images
    }
    return HttpResponse(template.render(context=context, request=request))


def contact(request):
    template = loader.get_template('meistrai_app/contact.html')
    return HttpResponse(template.render(context=None, request=request))


def about(request):
    template = loader.get_template('meistrai_app/about.html')
    return HttpResponse(template.render(context=None, request=request))


def services(request):
    template = loader.get_template('meistrai_app/services.html')
    return HttpResponse(template.render(context=None, request=request))
