from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
    now = datetime.now()
    template = loader.get_template('l2l/index.html')
    context = {
        'iso': now.strftime("%Y-%m-%dT%H:%M:%S"),
        'now': now
    }
    return HttpResponse(template.render(context, request))

def upload(response):
    return render(response, "l2l/upload.html", {})
