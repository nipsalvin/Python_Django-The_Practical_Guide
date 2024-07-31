from django.shortcuts import render
from django.http import HttpResponse

from .models import Meetup

# Create your views here.
def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'meetups' : meetups,
    })

def meetup_details(request, meetup_slug):
    try:
        meetup = Meetup.objects.get(slug=meetup_slug)
        # import ipdb; ipdb.set_trace()
        context = {
            'meetup': meetup,
            'meetup_found' : True,
        }
        return render(request, 'meetups/meetup-details.html', context)
    except Exception as exc:
        context = {
            'meetup_found':False
        }
        return render(request, 'meetups/meetup-details.html', context)