from django.shortcuts import render,get_object_or_404
from .models import Listening
from agents.models import Agent
# Create your views here.

def index(request):
    homes = Listening.objects.all()[:6]
    agents = Agent.objects.all()[:4]

    return render(request,'shelter/index.html',{'homes':homes,'agents':agents})


def propertiesList(request):
    homes = Listening.objects.all()[:9]
    return render(request,'shelter/properties_list.html',{'homes':homes})

def propertyDetail(request,slug):
    sidebar_homes = Listening.objects.all()[:3]
    home = get_object_or_404(Listening,slug=slug,available=True)
    return render(request,'shelter/property_detail.html',{'home':home,'sidebar_homes':sidebar_homes})
