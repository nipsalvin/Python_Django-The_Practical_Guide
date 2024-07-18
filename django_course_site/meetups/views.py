from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups = [
        {'title' : 'The first meetup'},
        {'title' : 'The second meetup'},
        {'title' : 'The third meetup'},
    ]
    # import ipdb; ipdb.set_trace()
    return render(request, 'meetups/index.html', {
        'meetups' : meetups,
        'show_meetups' : False,
    })