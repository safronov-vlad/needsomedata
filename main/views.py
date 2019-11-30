from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.template.context_processors import csrf

from .models import *

def default_context(request):
    c = {}
    c.update(csrf(request))
    return {'c': c}

def check_login(request):
    if request.session['user']:
        if request.session['user_type'] == 'userlow':
            return UserLow.objects.get(pk=request.session['user'])
        else:
            return Zhilishniki.objects.get(pk=request.session['user'])

def index(request):
    template = loader.get_template('index.html')

    context_data = default_context(request)

    return HttpResponse(template.render(context_data))

def login(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'userlow':
            request.session['user_type'] = 'userlow'
            request.session['user'] = UserLow.objects.get(pk=request.POST.get('email')).pk
        else:
            request.session['user_type'] = 'bussinesuser'
            request.session['user'] = Zhilishniki.objects.get(pk=request.POST.get('email')).pk

    return redirect('/userarea/')

def userarea(request):
    template = loader.get_template('userarea.html')

    context_data = default_context(request)

    user = check_login(request)

    try:
        if not request.session['user']:
            return redirect('/')
    except:
        request.session['user'] = False
        return redirect('/')

    context_data.update({
        'user': user,
    })

    context_data.update({
        'trichcodes': user.user_trichcodes.all().order_by('-pk')
    })

    return HttpResponse(template.render(context_data))