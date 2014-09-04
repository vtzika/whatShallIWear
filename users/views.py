from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello!!! Do you want to be recommended? Let's start!!!")


def gender(request):
    return HttpResponse("Can you provide me your gender?")



def location(request):
    return HttpResponse("Can you provide me your location?")