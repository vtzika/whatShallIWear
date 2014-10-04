from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, Context
from django.template.loader import get_template


def index(request, user_id):
    t = get_template('index.html')
    index = t.render(Context(request, {'uid': user_id}))
    return HttpResponse(index)



def gender(request):
    return HttpResponse("Can you provide me your gender?")



def location(request):
    return render(request, 'location.html')
