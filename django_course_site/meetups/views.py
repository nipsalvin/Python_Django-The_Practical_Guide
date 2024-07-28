from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups = [
        {
            'title' : 'The first meetup', 
            'location':'Nairobi',
            'slug':'first-meetup'
        },
        {
            'title' : 'The second meetup', 
            'location':'Nairobi',
            'slug':'second-meetup'
        },
        {
            'title' : 'The third meetup', 
            'location':'Nairobi',
            'slug':'third-meetup'
        },
    ]
    return render(request, 'meetups/index.html', {
        'meetups' : meetups,
        'show_meetups' : False,
    })

def meetup_details(request, meetup_slug):
    meetup = {
        'title' : 'The first meetup', 
        'location':'Nairobi',
        'slug':'first-meetup',
        'description':'This is the first meetup'
    }
    # import ipdb; ipdb.set_trace()
    return render(request, 'meetups/meetup-details.html', meetup)