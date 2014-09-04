from django.http import HttpResponse
from django.shortcuts import render
from sources.models import Source
from outfits.models import Outfit


def recommend(request, location=None, gender=None):
    source = chooseOutfitFromSource(Source(location=location, gender=gender))
    return HttpResponse(source)

def chooseOutfitFromSource(Source):
    Source.location