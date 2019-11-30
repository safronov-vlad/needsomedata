from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import *


def index(request):
    template = loader.get_template('index.html')

    context_data = {

    }

    return HttpResponse(template.render(context_data))