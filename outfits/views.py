from django.http import HttpResponse
from django.shortcuts import render
from sources.models import Source
from outfits.models import Outfit
from users.models import User


def recommend(request, location=None):
    #user = User.objects.get(user_id=user_id)
    #location = user.location
    #gender = user.gender
    #source = Source.objects.get(location=location, gender=gender)
    #return HttpResponse(source.source_url)
    return HttpResponse("Recomended to you %s" % location )

def chooseOutfitFromSource(Source):
    Source.location